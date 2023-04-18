#! /usr/bin/python3


#refer to 

#Maze representation:
#list of list of characters? or should it be a list of lava blobs that move?
#lava representation (>, row, col)\

#state
numrows:int = 0
numcols:int = 0

class path:
    def __init__(self, curr_loc:tuple[int, int], history:list[tuple[int, int]], directions:list[str] ):
        self.curr_loc = curr_loc
        self.history = history
        self.directions = directions
    def __str__(self):
        return f"{self.curr_loc}, History: {self.history}\n"
    def path(self):
        return self.history
    def __eq__(self, other):
        return self.curr_loc == other
    def __hash__(self):
        return hash(self.curr_loc)

#breadth first maze solver
#a 'state' is a list of lava locations
class state:
    def __init__(self, my_loc:list[path], lava:list[tuple()], numsteps:int):
        self.my_loc = my_loc
        self.lava = lava
        self.numsteps = numsteps
    def __str__(self):
        ret = ""
        for p in self.my_loc:
            ret += f"{p}" + ", "
        return ret + f"numsteps: {self.numsteps}\nLava: {self.lava}"


def process_input(filename):
    
    with open(filename) as f:
        lava = []
        global numrows
        global numcols
        lines = f.readlines()
        numcols = len(lines[0]) - 1 #skip the newline
        numrows = len(lines)
        for row in range(0,numrows):
            for col in range(0, numcols):
                char = lines[row][col]
                if char == '#':
                    lava.append((char, row, col))
                elif char != '.':
                    lava.append((char, row, col))
        return state([path((0,1), None, None)], lava, 0)

def generate_next_lava(curr_state):
    next_lava = []
    for pool in curr_state.lava:
        newrow:int
        newcol:int
        match pool[0]:
            case '>':
                newrow = pool[1]
                newcol = pool[2] + 1
            case '<':
                newrow = pool[1]
                newcol = pool[2] - 1
            case '^':
                newrow = pool[1] - 1
                newcol = pool[2] 
            case 'v':
                newrow = pool[1] + 1
                newcol = pool[2]
            case '#':
                next_lava.append(pool)
                continue
                
        #Check for wrapping in a really lazy way
        if newrow == 0:
            newrow = numrows - 2
        elif newrow == numrows - 1:
            newrow = 1
        if newcol == 0:
            newcol = numcols - 2
        elif newcol == numcols - 1:
            newcol = 1
        next_lava.append((pool[0], newrow, newcol))

    return next_lava

def is_lava(lava, loc):
    if loc[0] < 0 or loc[0] > numrows:
        return False
    if loc[1] < 0 or loc[1] > numcols:
        return False
    for l in lava:
        if l[1] == loc[0] and l[2] == loc[1]:
            return False
    return True

def generate_next_state_bfs(states:state):
    next_lava = generate_next_lava(states)
    new_locs = []
    new_dist = states.numsteps + 1
    for p in states.my_loc:
        #print("TESTING LOC:\n {}", p)
        #print(f"loc: {p.curr_loc} pre_history: {p.history}\n\tdirections to here: {p.directions}" )
        loc = p.curr_loc
        if p.history is None:
            new_history = [loc]
            new_directions = ["start"]
        else:
            new_history = p.history + [loc]
            new_directions = p.directions
        #print(f"new_history: {new_history}")
        #try and go each direction
        left = tuple([loc[0], loc[1] - 1])
        right = tuple([loc[0], loc[1] + 1])
        down = tuple([loc[0] + 1, loc[1]])
        up = tuple([loc[0] - 1, loc[1]])
        if (is_lava(next_lava, loc)):
            #print("appending loc")
            new_locs.append(path(loc, new_history, new_directions + ["wait"]))
        if (is_lava(next_lava, left)):
            #print("appending left")
            new_locs.append(path(left, new_history, new_directions + ["left"]))
        if (is_lava(next_lava, right)):
            #print("appending right")
            new_locs.append(path(right, new_history, new_directions + ["right"]))
        if (is_lava(next_lava, down)):
            #print("appending down")
            new_locs.append(path(down, new_history, new_directions + ["down"]))
        if (is_lava(next_lava, up)):
            #print("appending up")
            new_locs.append(path(up, new_history, new_directions + ["up"]))
        #remove duplicate locations, everyone here i on the same step:
        no_dups = [*set(new_locs)]
    return state(no_dups, next_lava, new_dist)

def solved(states):
    for p in states.my_loc:
        if (numrows-1, numcols -2) == p.curr_loc:
            #print("Curr_loc:")
            #print(p.curr_loc)
            #print("History")
            #print(p.history)
            return True
    return False

def get_solved(states):
    ret = []
    for p in states.my_loc:
        if (numrows-1, numcols -2) == p.curr_loc:
            print("Curr_loc:")
            print(p.curr_loc)
            print("History")
            print(p.history)
            return p

def pretty_print(input:state) -> None:
    print("Lava: ")
    for pool in input.lava:
        print(pool)
   

def main():
    curr_state = process_input("realmaze.txt")
    count = 0
    while(not solved(curr_state)):
        print(count)
        count += 1
        curr_state = generate_next_state_bfs(curr_state)
    #pretty_print(curr_state)
    #curr_state = generate_next_state(curr_state)
    pretty_print(curr_state)
    solution_path = get_solved(curr_state)
    solution = solution_path.history + [solution_path.curr_loc]
    print(solution_path.directions)
    print(solution)
    num_steps = len(solution) - 1 #skip the initial location (number of steps not locations)
    print(f"num steps: {num_steps}")
    print("SOLVED")
main()


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
        return lava, numrows, numcols
    
def print_maze(lava, numrows, numcols):
    maze = [['.' for col in range(numcols)] for row in range(numrows)]
    for pool in lava:
        if maze[pool[1]][pool[2]] == '.':
            maze[pool[1]][pool[2]] = pool[0]
        elif str(maze[pool[1]][pool[2]]) in "<>^v":
            maze[pool[1]][pool[2]] = str(2)
        else:
            maze[pool[1]][pool[2]] = str(int(maze[pool[1]][pool[2]]) + 1)
    for row in maze:
        for character in row:
            print(f"{character}", end='')
        print()   
    return maze         

def generate_next_lava(lava):
    next_lava = []
    for pool in lava:
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

def main():
    lava, numrows, numcols = process_input("realmaze.txt")
    for i in range(7):
        print(f"Day {i}")
        print_maze(lava, numrows, numcols)
        lava = generate_next_lava(lava)
    print(f"Day 7")
    maze = print_maze(lava, numrows, numcols)
    print(f"CHAD{{{''.join(maze[1])}}}")

main()
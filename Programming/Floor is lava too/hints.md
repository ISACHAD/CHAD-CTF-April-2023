### Hint 1
Check for off by one errors, the maze is not a square and flipping the dimmensions once will cause chaos.

### Hint 2
Your algorithm needs to be pruning the search tree AGGRESSIVELY. We don't care about the final path, so don't keep multiple positions that are the same (assuming the same number of steps to get there). You might have an algorithm that works but works too slowly, my solution took roughly a minute to run... (on an i5 9600k if anyone cares) I know you can do better!

### Hint 3
The solution is between 150 and 300. If you are exceeding these bounds something is WRONG.
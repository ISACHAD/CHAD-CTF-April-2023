# The floor is lava and its moving!

## Medium
### Scenario
We are a part of TheLavaChannel and we forcast the position of lava over time. 
We are looking to find a way out of here! Think of this as a maze solver, but the maze moves every round and we can't die. The input looks something like this.
```
#.#####
#.....#
#.>...#
#.....#
#.....#
#...v.#
#####.#
```

The pools of lava flow in the direction they are created, and each 'round' they move one square. Anything about to wrap wraps around the maze.

```
#.#####
#...v.#
#..>..#
#.....#
#.....#
#.....#
#####.#
```

When lava hits each other they both occupy the same square, and it is displayed as a number as such, but they continue to go in the direction they were orignally, here are the next two iterations of the lava.

```
#.#####
#.....#
#...2.#
#.....#
#.....#
#.....#
#####.#

#.#####
#.....#
#....>#
#...v.#
#.....#
#.....#
#####.#
```

As a lava forecaster, I need you to to tell me where the lava will be in a week! starting with iteration on day 0, i need a map of the lava on day 7.

Here is a **sample** that you can test your code against.
### Sample input
```
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
```
### Sample Solution with intermediate steps
```
Day1
#.###### 
#.>3.<.#
#<..<<.#
#>2.22.#
#>v..^<#
######.#

Day2
#.######
#.2>2..#
#.^22^<#
#.>2.^>#
#.>..<.#
######.#

Day3
#.######
#<^<22.#
#.2<.2.#
#><2>..#
#..><..#
######.#

Day4
#.######
#.<..22#
#<<.<..#
#<2.>>.#
#.^22^.#
######.#

Day5
#.######
#2.v.<>#
#<.<..<#
#.^>^22#
#.2..2.#
######.#

Day6
#.######
#>2.<.<#
#.2v^2<#
#>..>2>#
#<....>#
######.#

Day7
#.######
#.22^2.#
#<v.<2.#
#>>v<>.#
#>....<#
######.#
```
Sample flag 
The Flag for this solution will be `CHAD{first_row of the lava}`, for example, the first row of the input as a solution would look like `CHAD{#.22^2.#}`

# Real input
```
#.##################################
#>>^<^v>v<>^>>v<<.<<<^<vv^<^>v><><>#
#>^>^><^v<>.v><><<<>><v><>vv^.><v.>#
#.>^>v<v^><v<v^><>^v>><>v<>^><>v.^>#
#<>^^^..v^^v^<<><<<^<>.>.vvv.v>^.<>#
#>v^vvv><>>v^v.v><v<<^.>.>>^<.^<<><#
#>^>^>^<<>^><<v^^^^^^^v^<<>>v^^><v>#
#><vv.vv^v.>^>>v<<<v^>>^^>><v<<.v^>#
#<^<v>.>^v^<v^^><vv.>>.<^>.^..><^^>#
#>^><v><<<>><^v^>v<><>v^><.v>>.>.v>#
#>vv>^.<<>><^>.<^><v<^<>>v><v>^.^<<#
#>^>v<^v^.<<v<<^^>^<>vvv<v^>^<v<.^<#
#>^<.^.<>v<.<^v>v<^^<>^>vvv..v.^v^>#
##################################.#
```

# SOLUTION
The Flag for this solution will be `CHAD{first_row of the lava}`, for example, the first row of the input as a solution would look like `CHAD{#>>^<^v>v<>^>>v<<.<<<^<vv^<^>v><><>#}`

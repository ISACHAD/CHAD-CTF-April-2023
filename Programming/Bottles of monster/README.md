# How many bottles of ~~Beer~~ Monster

### Easy

We are all familliar with the classic song, 99 bottles of ~~Beer~~ monster on the wall, if not here is how it goes:

```
99 bottles of monster on the wall, 99 bottles of monster. Take one down, pass it around, 98 bottles of monster on the wall
98 bottles of monster on the wall, 98 bottles of monster. Take one down, pass it around, 97 bottles of monster on the wall
97 bottles of monster on the wall, 97 bottles of monster. Take one down, pass it around, 96 bottles of monster on the wall
etc, etc
1 bottles of monster on the wall, 1 bottles of monster. Take one down, pass it around, 0 bottles of monster on the wall
```

### Step 1
I am very weird so i want to know what every number that is said in the song, adds up to. 

For example the first line is 99 + 99 + 98 = 296, then you go on to the next line and keep going for the entire song.

### Step 2
Come to think of it, this is too easy for an easy problem. I wanna make sure you printed out the lyrics to the whole song! So what I want as the flag, is the characters from (sum of all numbers in the song) to (sum of all numbers in the song + 20). The number will be much larger than the characters in a single song, so you might have to sing it again!

### Some help
Here is my python format string for an arbitrary line in the song.
`f"{i} bottles of monster on the wall, {i} bottles of monster. Take one down, pass it around, {i-1} bottles of monster on the wall\n"`



### Flag
The flag will look something like this: `CHAD{bottles of monster. }`
*note the flag could start or end with a space, but i promise there is no newline in it.
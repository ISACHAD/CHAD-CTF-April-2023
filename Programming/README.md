# Writeups for Programming Problems

**Owen Gruss**

## Flags
[Easy]
rEEEEEgex: `CHAD{insignificantpelicans}`
Bottles of Monster: `CHAD{er on the wall, 78 b}`

[medium]
Floor is lava: `CHAD{#>2>.>.>32^<<23<.>.2>.v.2.<^v..<^2.#}`
Rusty: N/A (coding challenge)

[hard]
Floor is lava too: `CHAD{228}`

## Summary
Here is a brief explanation of how to solve each of the problems

### rEEEEEgex
Regex can be super helpful in every coders/hackers life. I would recommend doing some quick online research about regex if you ahve never before used it. 

For our problem we were looking for words with specific features, and even if you anen't perfect with the expression it will very easily get you super close.

My command: `grep -P "^[pi].*(?:ican)(^')*[st]" american-english-small`

Something as simple as `grep -P "ican" american-english-small` will get you down to a handful or words already.

### How many bottles of ~~beer~~ monster
The goal of this problem was to mess around with some strings in a few tricy ways. I have implemented a solution in python that you can now see. 

Strings are a common place in programming and sometimes you have to do weird things with them, hopefully you learned some neat python features to help you! Or any language you used for that matter! The largest goal was to ensure everyone has an environment in which they can write code and do odd things.

### Rusty
Everyone knows python these days, so I wanted to challenge you all in a different way. Since CTFd can run your code for you, I am forcing you all to use RUST!!!! MUAHAHAHAHAHA.

Setting up a rust environment and learning the basic syntax was the core of this challenge. I hope you all don't hate rust now as it is a fascinating language with a surprising amount of features. I solved this problem in a way the leverages some unique rust features so hopefully this introduction will get you all excited.

For solving this problem, I would recommend solving it in your favorite language and then figuring out how to convert it to rust. The challenge itself is very easy if you have done rust before. 

### The Floor is Lava
The goal of this challenge was to stretch your data structure knowledge a little bit and keep you on your toes with off by one errors. 

I implemented all of this without classes but this type of problems lends itself well to an object oriented nature, and that could ba  large benefit as we will learn in part too. 

The trickiest parts of simulation is representing the 'map', I chose to do it in a lava focused manner, where I kept a list of lava pools, consisting of their direction and location. I later included the walls in this list as well, as non moving lava blobs.
Also the location wrapping of the lava, is a tricky thing to get your head arround when looking at coordinates. It is extremely easy to get off by one and have an incorrect solution along the way.

Then converting back from a list of lava pools to a map representation took some more data moving but overall this problem doesn't involve any super tricky things.

### The Floor is Lava too
We all knew this was a maze all along! Now it is time to solve it.

The goal was to bring everyone back to algorithms class and see those efficiency muscles flex. 

The first time i attempted this problem I got the test maze and was super excited, only to learn i could only get to step ~50 before my computer was taking minutes per step.... 

Since this is a moving maze, the decision tree is much more obfuscated but can be built. When you have a tree, you have ALGORITHMS!!!

I did not take this approach although i might by the time the CTF happens. I opted for a different route, a HEAVILY pruned BFS which got my runtime to a manageable state thanks the many many pools of lava cutting off a lot of my paths. 

TODO more of this writeup
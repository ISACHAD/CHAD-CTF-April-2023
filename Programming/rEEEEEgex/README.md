# rEEEEEgex is king

### Easy

You have probably heard of regex before, if you have never heard of it before there are some really good resources at the bottom.

The easiest way try this problem is download the dictionary and run `grep -p "regex" american-english-small`


We are looking for two words that we will put together and create the flag.
 - 'ican' is somewhere within each word. Such as Amer**ican**. 
 - the words end in `s` and `t`
 - one of the words start with `p` and another with `i`
 - there is no `'` in the word
-  the words go together in alphabetical order


There are a lot of ways to sovle this puzzle! I would recommend ignoring the `'` requirement and put the words together if you are struggling. Can be a fun challenge to get down to the two words though!


### How to test your regex easily
https://regex101.com/
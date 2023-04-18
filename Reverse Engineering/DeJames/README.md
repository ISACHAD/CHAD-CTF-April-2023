# Description
What the heck, this thing doesn't do anything????

*Remember the flag is in CHAD{flag} format*

Author: D̸́̉3̷̐̌#6194

# Flag
CHAD{s33!_tH@t_wAsNt_s0_bAd!}

# Hints

## Hint 1
Ghidra can help us see what's going on under the hood. There's certainly no argument there.

# Walkthrough
Executing the application seems output "Starting application" and then it just ends.  

Examining the binary further in ghidra/ida/gdb/etc should reveal that it is checking for the following argument:  
```./DeJames cHaD```
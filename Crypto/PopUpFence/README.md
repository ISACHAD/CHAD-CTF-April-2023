# Chained

Created by Tate Bowers  
Category: Easy

## Story
Alan had a brilliant idea to use already sent messages to encrypt new messages!  
He could take the plaintext of the old message, which was secure, to secure the plaintext of the new message.  That had to be secure, right?  
Then we rummaged through Beth's garbage and recovered one of the messages.

## Structure

The Challenge consists of the intercepted message, and three ciphertexts

## Overview  

- This challenge teaches people the basics of XOR.   
- Theoretically, this could be done without the intercepted message with enough ciphertext, since it's not random  

## Solution/Walthrough  

- This challenge is pretty easily done in Cyberchef  
- Use the intercepted message as the input for xor, and read in the ciphertext from hex  
- Take the output as the input for xor  
- repeat one more time   

FLAG: `CHAD{Imp3rfect_f0rward_s3curity-XXXX}`

# Hints
1. Cyberchef can help with visualizations  

## Notes
- [Introduction to One-Time Pads](https://en.wikipedia.org/wiki/One-time_pad)

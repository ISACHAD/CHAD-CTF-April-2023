import math
import string
import random

def otp(plaintext: bytes, pad: bytes):

    ciphertext = b''
    final_pad = pad
    
    if len(pad) < len(plaintext):
    
        for i in range(0, math.ceil(len(plaintext)/len(pad))):
            final_pad = final_pad+pad
        
    final_pad = final_pad[0:len(plaintext)]
    
    for x, y in zip(plaintext, final_pad):
        ciphertext += (x^y).to_bytes(1,'little')
    
    return ciphertext

def generate_flag(plaintext, joke, length=4):
    flag_start = "flag{"
    flag_joke = joke
    flag_random = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=length))
    flag_end = "}"

    return f"{plaintext}{flag_start}{flag_joke}-{flag_random}{flag_end}"

def generate_pad(length: int, seed: int = -1):

    if seed != -1:
        random.seed(seed)
        
    ret = bytes([random.randrange(0, 256) for _ in range(0, length)])
            
    return ret


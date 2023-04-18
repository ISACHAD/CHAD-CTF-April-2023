# Auto-oops 

I saw a cipher online and tried to make my own version. There's no way my cipher has any weakness and you'll never get the flag!

Here is the encrypted flag: `u2s3rd7tfz_5n62e{d_uj1e?wpuu{3}4pay_flat 4gf8sshbfy 1_gqt}q{tfy6m2a6j{jq5 64px19x56x}8} 485}_9b_u7h6r_p{2jhakg6y`

*Remember the flag is in CHAD{flag} format*

Author: \_mac\_#4656

## Solution

Looking at the source, it appears to rotate each of the first `key_len` bytes by the corresponding byte in the key, then if the plaintext is longer than the key, rotates the following values by the byte in the ciphertext at `i - key_len` where `i` is the index of the current byte.

First I reversed the first section using the flag format as a crib to get the key:
If you try using a crib as the flag format to get the key, it doesn't quite work.
```py
alpha_num = "abcdefghijklmnopqrstuvwxyz1234567890_{}? "
alpha_len = len(alpha_num)
ct = "u2s3rd7tfz_5n62e{d_uj1e?wpuu{3}4pay_flat 4gf8sshbfy 1_gqt}q{tfy6m2a6j{jq5 64px19x56x}8} 485}_9b_u7h6r_p{2jhakg6y"
crib = 'chad{'

for i in range(len(crib)):
    key += alpha_num[alpha_num.index(ct[i]) - alpha_num.index(crib[i]) % alpha_len]
print(key)
```
this prints:
```
suszv
```

Which is somewhat concerning since it doesn't repeat any characters, which implies that the length of the key is either exactly 6 or longer. The key is not necessary for decoding the rest of the ciphertext since it is encoded using previous parts of the ciphertext which are known, but knowing the key length is important for knowing how large that offset is.

Since we don't see any repeats in the key found from the crib attack, we'll just start guessing key lengths starting with 6 until something coherent shows up. Luckily that happens at `key_len = 8`, and the following code appended to the snippet above will print a flag (full code in `solve.py`):

```py
flag += crib
key_len = 7

for i in range(len(key), len(ct)):
    flag += alpha_num[alpha_num.index(ct[i]) - alpha_num.index(ct[i-key_len]) % alpha_len]
print(flag)
```

and that outputs:
```
chad{think i might actually have some flaws in this poorly implemented autokey cipher chad{ch3ck_y0ur_cryp70}
```

And we have our flag! In hindsight looking at the output, our crib was likely very wrong and the start of the plaintext is something entirely different, but lucky for us our flag is at the end of the message.
```
CHAD{ch3ck_y0ur_cryp70}
```

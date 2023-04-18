#!/usr/bin/env python3

alpha_num = "abcdefghijklmnopqrstuvwxyz1234567890_{}? "
flag = "REDACTED"
key = "REDACTED"

def encrypt(msg, key, alpha_num):
	msg_len = len(msg)
	key_len = len(key)
	alpha_len = len(alpha_num)
	ciphertext = ""
	
	for i in range(msg_len):
		if i >= key_len:
			ciphertext += alpha_num[(alpha_num.index(msg[i]) + alpha_num.index(ciphertext[i - key_len])) % alpha_len]
		else:
			ciphertext += alpha_num[(alpha_num.index(msg[i]) + alpha_num.index(key[i])) % alpha_len]
	return ciphertext


enc_flag = encrypt(flag, key, alpha_num)
print("Here is the encrypted flag: %s" % enc_flag)


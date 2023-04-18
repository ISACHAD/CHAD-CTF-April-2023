import challenge_basis

def generate_challenge_1():
    
    joke = "Imp3rfect_f0rward_s3curity"
    
    dissov_reference = "Hi Beth, here's another message I'm sending you."
    cipher_ref_num_0 = "The supersecretly amazingly awesomely message is"
    cipher_ref_num_1 = "going to be sent to you in another iterated note"
    cipher_ref_num_2 = "which is "
    
    cipher_ref_num_2 = challenge_basis.generate_flag(cipher_ref_num_2, joke, 0)
    
    ciphertext = challenge_basis.otp(dissov_reference.encode(), cipher_ref_num_0.encode())
    print(f"ciphertext0: {ciphertext} -> {ciphertext.hex()}\n")
    ciphertext = challenge_basis.otp(cipher_ref_num_1.encode(), cipher_ref_num_0.encode())
    print(f"ciphertext1: {ciphertext} -> {ciphertext.hex()}\n")
    ciphertext = challenge_basis.otp(cipher_ref_num_2.encode(), cipher_ref_num_1.encode())
    print(f"ciphertext2: {ciphertext} -> {ciphertext.hex()}\n")
    
generate_challenge_1()

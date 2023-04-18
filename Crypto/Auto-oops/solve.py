CHAR_SPACE = "abcdefghijklmnopqrstuvwxyz1234567890_{}? "
ALPHA_LEN = len(CHAR_SPACE)

flag = ''
ct = 'u2s3rd7tfz_5n62e{d_uj1e?wpuu{3}4pay_flat 4gf8sshbfy 1_gqt}q{tfy6m2a6j{jq5 64px19x56x}8} 485}_9b_u7h6r_p{2jhakg6y'

def decrypt(ct, k):
    pt = ''
    key_len = len(k)
    for i in range(key_len, len(ct)):
        pt += CHAR_SPACE[CHAR_SPACE.index(ct[i]) - CHAR_SPACE.index(ct[i-key_len]) % ALPHA_LEN]

    return pt


print("CRACKING CIPHERTEXT: %s\n" % ct)

crib = ''

while('chad{' not in flag):
    crib += 'a'
    flag = decrypt(ct, crib)

print("FLAG FOUND: %s" % flag)


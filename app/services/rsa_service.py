import json

# ===================================
# ENCRYPT RSA
# ===================================

def encrypt_text_rsa(plaintext, public_key):

    e, n = public_key

    ciphertext = []

    for char in plaintext:

        m = ord(char)

        c = pow(m, e, n)

        ciphertext.append(c)

    return ciphertext


# ===================================
# DECRYPT RSA
# ===================================

def decrypt_text_rsa(ciphertext, private_key):

    d, n = private_key

    plaintext = ""

    for c in ciphertext:

        m = pow(c, d, n)

        plaintext += chr(m)

    return plaintext
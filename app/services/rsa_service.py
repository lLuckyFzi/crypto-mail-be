import random
from app.utils.math_utils import gcd, mod_inverse

def generate_rsa_keys():
    # Pilih dua bilangan prima (Untuk MVP/Edukasi, kita pakai yang statis/kecil)
    # Di sistem production, ini harus di-generate secara random dengan ukuran 2048-bit
    primes = [89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163]
    p = random.choice(primes)
    q = random.choice([x for x in primes if x != p])
    
    # Hitung n dan phi
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Cari e (Public Key Exponent)
    e = 3
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 2
        
    # Cari d (Private Key Exponent)
    d = mod_inverse(e, phi)
    
    # Mengembalikan tuple: (Public Key, Private Key)
    return {"e": e, "n": n}, {"d": d, "n": n}
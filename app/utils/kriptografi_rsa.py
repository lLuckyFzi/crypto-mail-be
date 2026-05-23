# app/utils/kriptografi_rsa.py

# Catatan: Kita bisa mengimpor math_utils nanti saat membuat endpoint 'daftar' 
# from app.utils.math_utils import gcd, mod_inverse

def dekripsi_rsa(ciphertext, d, n):
    """
    Fungsi untuk mendekripsi pesan menggunakan kunci privat (d, n).
    """
    # Jika ciphertext tersimpan sebagai string teks (contoh: "142, 253, 532")
    if isinstance(ciphertext, str):
        # Pisahkan berdasarkan koma dan ubah menjadi list angka
        ciphertext_list = [int(c.strip()) for c in ciphertext.split(',') if c.strip()]
    else:
        ciphertext_list = ciphertext

    pesan_asli = ""
    for char_cipher in ciphertext_list:
        # Rumus utama RSA Dekripsi: M = C^d mod n
        # pow(nilai, pangkat, modulo) adalah bawaan Python yang sangat cepat
        char_asli = pow(int(char_cipher), d, n)
        pesan_asli += chr(char_asli)
        
    return pesan_asli
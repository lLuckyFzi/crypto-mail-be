# app/controllers/decrypt_pesan.py
from flask import request, jsonify
from app.utils.kriptografi_rsa import dekripsi_rsa

def dekripsi_pesan_controller():
    data = request.get_json()
    
    ciphertext = data.get('ciphertext')
    private_key = data.get('private_key') # Diharapkan berbentuk dict {"d": angka, "n": angka}

    if not ciphertext or not private_key:
        return jsonify({"error": "Data ciphertext dan private_key dibutuhkan!"}), 400

    try:
        # Mengambil nilai d dan n dari input user
        d = private_key.get('d')
        n = private_key.get('n')

        if not d or not n:
            return jsonify({"error": "Kunci privat harus terdiri dari komponen 'd' dan 'n'"}), 400

        # Memanggil fungsi RSA
        pesan_terbaca = dekripsi_rsa(ciphertext, d, n)

        return jsonify({
            "status": "sukses", 
            "ciphertext_asli": ciphertext,
            "pesan_terbaca": pesan_terbaca
        }), 200
        
    except Exception as e:
        return jsonify({"error": f"Gagal memproses RSA: {str(e)}"}), 500
# app/controllers/get_pesan.py
from flask import request, jsonify
from app.models.message_model import Message # Asumsi nama model tetap menggunakan Message

def ambil_pesan():
    # Mengambil ID user sebagai penerima pesan
    receiver_id = request.args.get('receiver_id')
    
    if not receiver_id:
        return jsonify({"error": "Parameter receiver_id dibutuhkan!"}), 400

    # Mencari semua pesan yang ditujukan ke receiver_id tersebut
    daftar_pesan = Message.query.filter_by(receiver_id=receiver_id).all()
    
    data_pesan = []
    for pesan in daftar_pesan:
        data_pesan.append({
            "id": pesan.id,
            "pengirim_id": pesan.sender_id,
            "penerima_id": pesan.receiver_id,
            "sender_name": pesan.sender.username if pesan.sender else f"User #{pesan.sender_id}",
            "ciphertext": pesan.ciphertext,
            "dibuat_pada": pesan.created_at.isoformat() if pesan.created_at else None
        })

    return jsonify({"status": "sukses", "data": data_pesan}), 200
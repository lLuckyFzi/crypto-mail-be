import json
from flask import request, jsonify
from app import db
from app.models.user_model import User
from app.models.message_model import Message

def send_message():
    data = request.get_json()

    receiver_id = data.get("receiver_id")
    ciphertext = data.get("ciphertext")
    sender_id = data.get("sender_id")

    if not sender_id or not receiver_id or not ciphertext:
        return jsonify({"status": "error", "message": "Data tidak lengkap"}), 400

    receiver = User.query.get(receiver_id)
    if not receiver:
        return jsonify({"status": "error", "message": "Receiver tidak ditemukan"}), 404

    try:
        new_message = Message(
            sender_id=sender_id,
            receiver_id=receiver_id,
            ciphertext=ciphertext
        )

        db.session.add(new_message)
        db.session.commit()

        return jsonify({
            "status": "success",
            "message": "Pesan berhasil dikirim dan dienkripsi."
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500
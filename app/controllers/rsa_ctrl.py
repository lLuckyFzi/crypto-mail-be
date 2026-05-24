import json

from flask import request, jsonify

from app import db

from app.models.user_model import User
from app.models.message_model import Message

from app.services.rsa_service import encrypt_text_rsa


# ===================================
# SEND MESSAGE
# ===================================

def send_message():

    data = request.get_json()

    sender_id = data.get("sender_id")
    receiver_id = data.get("receiver_id")
    message = data.get("message")

    # VALIDASI
    if not sender_id or not receiver_id or not message:

        return jsonify({
            "status": "error",
            "message": "Data tidak lengkap"
        }), 400

    # CEK RECEIVER
    receiver = User.query.get(receiver_id)

    if not receiver:

        return jsonify({
            "status": "error",
            "message": "Receiver tidak ditemukan"
        }), 404

    # AMBIL PUBLIC KEY RECEIVER
    public_key = (
        int(receiver.public_key_e),
        int(receiver.public_key_n)
    )

    # ENCRYPT MESSAGE
    ciphertext = encrypt_text_rsa(
        message,
        public_key
    )

    # SIMPAN KE DATABASE
    new_message = Message(
        sender_id=sender_id,
        receiver_id=receiver_id,
        ciphertext=json.dumps(ciphertext)
    )

    db.session.add(new_message)
    db.session.commit()

    return jsonify({
        "status": "success",
        "ciphertext": ciphertext
    }), 201
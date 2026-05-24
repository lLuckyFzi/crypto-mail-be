from flask import request, jsonify

from app.models.user_model import User


# ===================================
# SEARCH USER
# ===================================

def search_user():

    username = request.args.get("username")

    if not username:

        return jsonify({
            "status": "error",
            "message": "Username kosong"
        }), 400

    users = User.query.filter(
        User.username.like(f"%{username}%")
    ).all()

    result = []

    for user in users:

        result.append({
            "id": user.id,
            "username": user.username,
            "public_key_e": user.public_key_e,
            "public_key_n": user.public_key_n
        })

    return jsonify({
        "status": "success",
        "data": result
    })
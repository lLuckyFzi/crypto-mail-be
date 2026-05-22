from flask import request, jsonify
from app.services.user_service import register_new_user, login_user

def register():
    try:
        data = request.get_json()
        
        if not data or 'username' not in data:
            return jsonify({"status": "error", "message": "Username wajib diisi"}), 400
            
        username = data['username'].strip()
        if len(username) < 3:
            return jsonify({"status": "error", "message": "Username minimal 3 karakter"}), 400
            
        result = register_new_user(username)
        
        return jsonify({
            "status": "success",
            "message": "Kunci berhasil dibuat.",
            "data": result
        }), 201
        
    except ValueError as e:
        return jsonify({"status": "error", "message": str(e)}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": "Terjadi kesalahan pada server"}), 500

def login():
    try:
        data = request.get_json()
        
        if not data or 'username' not in data:
            return jsonify({"status": "error", "message": "Username wajib diisi"}), 400
            
        username = data['username'].strip()
        
        result = login_user(username)
        
        return jsonify({
            "status": "success",
            "message": "Berhasil terhubung ke jaringan.",
            "data": result
        }), 200
        
    except ValueError as e:
        return jsonify({"status": "error", "message": str(e)}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": "Terjadi kesalahan server"}), 500
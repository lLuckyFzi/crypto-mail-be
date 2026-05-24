from app import db
from app.models.user_model import User
from app.services.rsa_service import generate_rsa_keys

def register_new_user(username):
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        raise ValueError("Username sudah terdaftar dalam jaringan.")
    
    public_key, private_key = generate_rsa_keys()
    
    new_user = User(
        username=username,
        public_key_e=str(public_key['e']),
        public_key_n=str(public_key['n'])
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    formatted_private_key = f"-----BEGIN RSA PRIVATE KEY-----\nd={private_key['d']}\nn={private_key['n']}\n-----END RSA PRIVATE KEY-----"
    
    return {
        "user_id": new_user.id,
        "username": new_user.username,
        "private_key": formatted_private_key
    }

def login_user(username):
    user = User.query.filter_by(username=username).first()
    
    if not user:
        raise ValueError("Username tidak ditemukan di jaringan.")
    
    return {
        "user_id": user.id,
        "username": user.username,
        "public_key_e": user.public_key_e,
        "public_key_n": user.public_key_n
    }

def cari_user_by_username(username):
    # Gunakan exact match (filter_by) agar output tidak bingung memilih array
    user = User.query.filter_by(username=username).first()
    
    if not user:
        return None
        
    return {
        "user_id": user.id,
        "username": user.username,
        "public_key_e": user.public_key_e,
        "public_key_n": user.public_key_n
    }
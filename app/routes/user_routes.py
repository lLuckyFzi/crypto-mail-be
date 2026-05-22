from flask import Blueprint
from app.controllers.user_ctrl import register, login

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/register', methods=['POST'])(register)
user_bp.route('/login', methods=['POST'])(login)
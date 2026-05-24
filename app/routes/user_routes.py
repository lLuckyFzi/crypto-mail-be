from flask import Blueprint
from app.controllers.user_ctrl import register, login, search_user

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/register', methods=['POST'])(register)
user_bp.route('/login', methods=['POST'])(login)
user_bp.route('/search', methods=['GET'])(search_user)
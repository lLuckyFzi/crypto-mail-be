# app/routes/pesan_routes.py
from flask import Blueprint

from app.controllers.get_pesan import ambil_pesan
from app.controllers.decrypt_pesan import dekripsi_pesan_controller
from app.controllers.rsa_ctrl import send_message

pesan_bp = Blueprint('pesan_bp', __name__)

# Menghubungkan URL dengan fungsi controller yang terpisah
pesan_bp.route('/', methods=['GET'])(ambil_pesan)
pesan_bp.route('/decrypt', methods=['POST'])(dekripsi_pesan_controller)
pesan_bp.route('/kirim', methods=['POST'])(send_message)
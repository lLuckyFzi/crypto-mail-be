from flask import Blueprint

from app.controllers.rsa_ctrl import send_message

rsa_bp = Blueprint(
    "rsa_bp",
    __name__
)

# ===================================
# SEND MESSAGE
# ===================================

@rsa_bp.route(
    "/send-message",
    methods=["POST"]
)
def send_message_route():

    return send_message()
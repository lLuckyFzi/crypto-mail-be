from flask import Blueprint

from app.controllers.user_ctrl import search_user

user_bp = Blueprint(
    "user_bp",
    __name__
)

# ===================================
# SEARCH USER
# ===================================

@user_bp.route(
    "/search",
    methods=["GET"]
)
def search_user_route():

    return search_user()
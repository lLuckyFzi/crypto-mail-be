from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)

    with app.app_context():

        from app.models.user_model import User
        from app.models.message_model import Message

        # IMPORT ROUTES
        from app.routes.rsa_routes import rsa_bp
        from app.routes.user_routes import user_bp

        # REGISTER BLUEPRINT
        app.register_blueprint(
            rsa_bp,
            url_prefix='/api/rsa'
        )

        app.register_blueprint(
            user_bp,
            url_prefix='/api/users'
        )

    @app.route('/api/status')
    def status():

        return {
            "status": "success",
            "message": "Backend CryptoMail menyala!"
        }

    return app
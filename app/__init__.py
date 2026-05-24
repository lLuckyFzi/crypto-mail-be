from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.routes.pesan_routes import pesan_bp

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    db.init_app(app)

    with app.app_context():
        from app.models.user_model import User
        from app.models.message_model import Message

    from app.routes.user_routes import user_bp

    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(pesan_bp, url_prefix='/api/pesan')
    
    @app.route('/api/status', methods=['GET'])
    def status():
        return {"status": "success", "message": "Backend CryptoMail menyala dengan baik!"}

    return app
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
    
    @app.route('/api/status', methods=['GET'])
    def status():
        return {"status": "success", "message": "Backend CryptoMail menyala dengan baik!"}

    return app
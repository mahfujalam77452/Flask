from flask import Flask
from app.routes.user import user_bp
from app.config import Config
from app.extensions import db

def create_app():
    app = Flask(__name__)

    
    app.config.from_object(Config)

    print(app.config["SECRET_KEY"])

    app.register_blueprint(user_bp)
    db.init_app(app)
    return app
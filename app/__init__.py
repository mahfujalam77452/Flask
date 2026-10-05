from flask import Flask
from app.routes.user import user_bp

def create_app(config=None):
    app = Flask(__name__)

    if config:
        app.config.from_mapping(config)

    app.register_blueprint(user_bp)

    return app
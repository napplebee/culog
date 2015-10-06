from flask import Flask
from configs import config

def create_app(environment_name):
    app = Flask(__name__)
    app.config.from_object(config[environment_name])

    from app.admin import admin as admin_bp
    from app.front import front as front_bp

    app.register_blueprint(admin_bp)
    app.register_blueprint(front_bp)

    return app

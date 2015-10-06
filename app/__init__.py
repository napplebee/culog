from flask import Flask
from flask.ext.security import SQLAlchemyUserDatastore
from app.core import db, security, bootstrap
from app.domain.users import User, Role
from configs import config


def create_app(environment_name):
    app = Flask(__name__)
    app.config.from_object(config[environment_name])

    db.init_app(app)
    bootstrap.init_app(app)
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, datastore=user_datastore)

    from app.admin import admin as admin_bp
    from app.front import front as front_bp

    app.register_blueprint(admin_bp)
    app.register_blueprint(front_bp)

    return app

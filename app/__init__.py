# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.security import SQLAlchemyUserDatastore
from flask_talisman import Talisman

from app.core import db, security, bootstrap
from app.data.users import User, Role
from configs import config
from app.error_handlers import register_err_handlers


def create_app(environment_name):
    app = Flask(__name__)
    csp = {
        'default-src': [
            '\'self\'',
            '\'unsafe-inline\'',
            'cookwith.love',
            'use.typekit.net',
            'fonts.googleapis.com',
            'js-agent.newrelic.com',
            'chs03.cookie-script.com',
            'mc.yandex.ru',
            'googletagmanager.com'
        ]
    }
    Talisman(app, content_security_policy=csp)
    app.config.from_object(config[environment_name])
    register_err_handlers(app)

    db.init_app(app)
    bootstrap.init_app(app)
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, datastore=user_datastore)

    from app.admin import admin as admin_bp
    from app.front import front as front_bp

    app.register_blueprint(admin_bp)
    app.register_blueprint(front_bp)


    return app

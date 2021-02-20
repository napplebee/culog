# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    BASE_EXTERNAL_URI = "http://cookwith.love"
    LOGO_PATH = "/static/front/logo.jpg"
    SUPPORTED_LANGS = ("ru", "en",)
    APP_BASE_DIR = os.path.join(basedir, "app")

    SECRET_KEY = os.environ.get('SECRET_KEY')
    BOOTSTRAP_SERVE_LOCAL = True
    SECURITY_PASSWORD_HASH = "sha512_crypt"
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT')
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 


config = {
    'culog': Config,
}

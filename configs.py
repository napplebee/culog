# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    BASE_EXTERNAL_URI = "http://cookwith.love"
    SUPPORTED_LANGS = ("ru", "en",)
    AMOUNT_TYPES = ("etc", "gr", "ml", "item")
    # SUPPORTED_LANGS = ("ru", "en", "sv",)
    APP_BASE_DIR = os.path.join(basedir, "app")

    SECRET_KEY = os.environ.get('SECRET_KEY')
    BOOTSTRAP_SERVE_LOCAL = True
    SECURITY_PASSWORD_HASH = "sha512_crypt"
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT')
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 

    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    # FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    # FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')


config = {
    'culog': Config,
}

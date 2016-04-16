# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    BASE_EXTERNAL_URI = "http://cookwith.love"
    SUPPORTED_LANGS = ("ru", "en",)

    SECRET_KEY = "cazk$ze&e^935+0t@fi18l78m%t+y5#-%ch#z$^!np##(d^"
    BOOTSTRAP_SERVE_LOCAL = True
    SECURITY_PASSWORD_HASH = "sha512_crypt"
    # SECURITY_PASSWORD_HASH = "bcrypt"
    SECURITY_PASSWORD_SALT = "$djU-ed!0_fR+#@@<PS[^@$clwiI("
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # SQLALCHEMY_DATABASE_URI = "sqlite:///{0}".format(os.path.join(basedir, 'data-dev1.sqlite'))
    SQLALCHEMY_DATABASE_URI = "postgres://eoophqgigqvgyw:E0GzQehWuVAZ2rMF0ECRiYa_6I@ec2-54-217-202-109.eu-west-1.compute.amazonaws.com:5432/d371u3mkfb1tfo"

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

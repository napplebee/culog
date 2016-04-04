# -*- coding: utf-8 -*-

from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security

db = SQLAlchemy()
bootstrap = Bootstrap()
security = Security()

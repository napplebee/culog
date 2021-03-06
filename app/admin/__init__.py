# -*- coding: utf-8 -*-

from flask import Blueprint

admin = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)

from . import forms, views

from flask import Blueprint

import os

static_path = os.path.join(os.path.dirname(__file__), "static/")
front = Blueprint(
    "front",
    __name__,
    static_folder="static",
    template_folder="templates",

)

from . import forms, views

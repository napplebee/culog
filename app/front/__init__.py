from flask import Blueprint

front = Blueprint(
    "front",
    __name__,
    static_folder="static",
    template_folder="templates",
)

from . import forms, views

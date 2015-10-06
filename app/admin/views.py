from . import admin


@admin.route("/")
def index():
    return "Hi admin"

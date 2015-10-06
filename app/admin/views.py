from . import admin
from flask.ext.login import login_required
from flask.ext.security import roles_required


@admin.route("/")
@login_required
@roles_required("root")
def index():
    return "Hi admin"

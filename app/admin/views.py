from . import admin
from app.admin.forms import BlogPostForm
from flask.ext.login import login_required
from flask.ext.security import roles_required
from flask import render_template


@admin.route("/")
@login_required
@roles_required("root")
def index():
    f = BlogPostForm()
    return render_template("admin/index.html", f=f)

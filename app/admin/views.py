from . import admin
from app.admin.forms import BlogPostForm
from flask.ext.login import login_required
from flask.ext.security import roles_required
from flask import render_template


@admin.route("/")
@login_required
@roles_required("root")
def index():
    return render_template("admin/base.html")


@admin.route("/blog/all")
@login_required
@roles_required("root")
def blog_post_list():
    # todo: read all posts
    posts = []
    return render_template("admin/blog/list.html", items=posts)


@admin.route("/blog/new", methods=["POST", "GET"])
@login_required
@roles_required("root")
def blog_post_new():
    f = BlogPostForm()
    title = "Create new post"
    return render_template("admin/blog/detail.html", v={
        "title": title,
        "f": f,
        "action": ""
    })


@admin.route("/blog/update", methods=["POST", "GET"])
@login_required
@roles_required("root")
def blog_post_update():
    f = BlogPostForm()
    return render_template("admin/blog/detail.html", f=f)


@admin.route("/blog/delete", methods=["POST", "GET"])
@login_required
@roles_required("root")
def blog_post_delete():
    pass

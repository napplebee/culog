from app.domain.blog_posts import BlogPost
from . import admin
from app.admin.forms import BlogPostForm
from flask.ext.login import login_required
from flask.ext.security import roles_required
from flask import render_template, request, url_for, redirect


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
    title = "Create new post"
    f = BlogPostForm()
    # if request.method == "POST" and f.validate():
    if request.method == "POST":
        post = BlogPost.populate_from_ui(f)
        post.save_to_db()
        return redirect(url_for('blog_post_list'))
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

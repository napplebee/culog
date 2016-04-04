# -*- coding: utf-8 -*-

from app.data.blog_posts import BlogPostHeader
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
    headers = BlogPostHeader.query.order_by(BlogPostHeader.updated_at.desc(), BlogPostHeader.created_at.desc()).all()
    posts = [
        {
            "id": h.id,
            "name": h.name,
            "created_at": h.created_at.strftime('%d.%m.%y %H:%M') if h.created_at else "", # move to template filter
            "updated_at": h.updated_at.strftime('%d.%m.%y %H:%M') if h.updated_at else "",
            "visible": h.visible
        } for h in headers
    ]
    return render_template("admin/blog/list.html", v={"posts": posts})

@admin.route("/blog/new", methods=["POST", "GET"])
@login_required
@roles_required("root")
def blog_post_new():
    f = BlogPostForm()
    # if request.method == "POST" and f.validate():
    if request.method == "POST":
        post = BlogPost.populate_from_ui(f)
        post.save()
        return redirect(url_for('.blog_post_list'))
    title = "Create new post"
    return render_template("admin/blog/detail.html", v={
        "title": title,
        "f": f,
        "action": ""
    })

@admin.route("/blog/update/<int:post_id>", methods=["POST", "GET"])
@login_required
@roles_required("root")
def blog_post_update(post_id):
    if request.method == "POST":
        f = BlogPostForm()
        post = BlogPost.populate_from_ui(f)
        post.update()
        return redirect(url_for('.blog_post_list'))
    else:
        post = BlogPost.populate_from_db(BlogPostHeader.query.get(post_id))
        title = "Update {0}".format(post.name)
        f = BlogPostForm(obj=post)

        return render_template("admin/blog/detail.html", v={
            "title": title,
            "f": f,
            "action": ""
        })

@login_required
@roles_required("root")
@admin.route("/post_preview/<int:post_id>")
def blog_post_preview(post_id):
    base_url = "en/{0}".format(request.url_root[:request.url_root.find("/", 8)])
    db_data = BlogPostHeader.query.get(post_id)
    post = BlogPost.populate_from_db(db_data, ["en"], base_url)
    return render_template("admin/blog/preview.html", v={
        "post": post
    })

@admin.route("/blog/delete", methods=["POST", "GET"])
@login_required
@roles_required("root")
def blog_post_delete():
    pass

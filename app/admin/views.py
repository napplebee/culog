# -*- coding: utf-8 -*-

from app.data.blog_posts import BlogPostHeader
from app.domain.blog_posts import BlogPost
from . import admin
from app.admin.forms import BlogPostForm
from flask.ext.login import login_required
from flask.ext.security import roles_required
from flask import render_template, request, url_for, redirect
from app.services.language_service import langService
from configs import Config as cfg
from . import new_forms as nf


@admin.route("/")
@login_required
@roles_required("root")
def index():
    return render_template("admin/base.html")


@admin.route("/blog/all")
@login_required
@roles_required("root")
def blog_post_list():
    headers = BlogPostHeader.query.order_by(BlogPostHeader.updated_at.desc(), BlogPostHeader.created_at.desc()).all()
    posts = [
        {
            "id": h.id,
            "name": h.name,
            "created_at": h.created_at.strftime('%d.%m.%y %H:%M') if h.created_at else "", # move strftime call to template filter
            "updated_at": h.updated_at.strftime('%d.%m.%y %H:%M') if h.updated_at else "",
            "visible": h.visible
        } for h in headers
    ]
    return render_template("admin/blog/list.html", v={
        "posts": posts,
        "supported_langs": cfg.SUPPORTED_LANGS
        })

@admin.route("/blog/new", methods=["POST", "GET"])
@login_required
@roles_required("root")
def blog_post_new():
    f = BlogPostForm()
    # if request.method == "POST" and f.validate():
    if request.method == "POST":
        post = BlogPost.populate_from_ui(f)
        post_id = post.save()
        return redirect("/admin/blog/update/{0}?saved".format(post_id))
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
        return redirect("/admin/blog/update/{0}?saved".format(post_id))
        # return redirect(url_for('.blog_post_list'))
    else:
        post = BlogPost.populate_from_db(BlogPostHeader.query.get(post_id))
        title = u"Update {0}".format(post.name)
        f = BlogPostForm(obj=post)

        return render_template("admin/blog/detail.html", v={
            "title": title,
            "f": f,
            "action": "",
            "saved": 1 if "saved" in request.args else 0
        })

@login_required
@roles_required("root")
@admin.route("/post_preview/<string:lang_override>/<int:post_id>")
def blog_post_preview(lang_override, post_id):
    current_lang, lang_fallback = langService.get_user_settings(request, lang_override)
    base_url = "{0}/{1}".format(lang_override, request.url_root[:request.url_root.find("/", 8)])
    db_data = BlogPostHeader.query.get(post_id)
    post = BlogPost.populate_from_db(db_data, lang_fallback, base_url)
    return render_template("admin/blog/preview.html", v={
        "post": post
    })

@login_required
@roles_required("root")
@admin.route("/post_list_preview/<string:lang_override>")
def blog_list_preview(lang_override):
    current_lang, lang_fallback = langService.get_user_settings(request, lang_override)
    db_data = BlogPostHeader.query.filter().order_by(BlogPostHeader.created_at.desc())
    base_url = "{0}/{1}".format(request.url_root[:request.url_root.find("/", 8)], current_lang)
    posts = [BlogPost.populate_from_db(d, lang_fallback, base_url) for d in db_data]
    return render_template("admin/blog/list_preview.html", v={
        "posts": posts
    })

@login_required
@roles_required("root")
@admin.route("/test/page")
def blog_test_page():
    # post = BlogPost.populate_from_db(BlogPostHeader.query.get(post_id))
    # title = u"Update {0}".format(post.name)
    # f = BlogPostForm(obj=post)
    #
    # return render_template("admin/blog/detail.html", v={
    #     "title": title,
    #     "f": f,
    #     "action": "",
    #     "saved": 1 if "saved" in request.args else 0
    # })

    form = nf.BlogPostForm()
    return render_template("admin/blog/test.html", v={
        "f": form
    })

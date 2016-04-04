# -*- coding: utf-8 -*-

from flask import render_template, request

from app.data.blog_posts import BlogPostHeader
from app.services.language_service import langService
from . import front as front_bp
from flask.ext.security import SQLAlchemyUserDatastore
from app import db, User, Role
from flask.ext.login import login_required
from flask.ext.security import roles_required
from app.domain.blog_posts import BlogPost



@front_bp.route("/<string:preferred_lang>")
@front_bp.route("/", defaults={"preferred_lang": "en"})
def index(preferred_lang):
    current_lang, lang_fallback = langService.get_user_settings(request)
    db_data = BlogPostHeader.query.filter(BlogPostHeader.visible).order_by(BlogPostHeader.created_at.desc()).limit(10)
    base_url = "{0}/{1}".format(request.url_root[:request.url_root.find("/", 8)], current_lang)
    posts = [BlogPost.populate_from_db(d, lang_fallback, base_url) for d in db_data]
    recent_posts = posts[:2]

    return render_template("front/test_index.html", v={
        "posts": posts,
        "recent_posts": recent_posts
    })


@front_bp.route("/<preferred_lang>/<path:post_url>")
def test_detail(preferred_lang, post_url):
    current_lang, lang_fallback = langService.get_user_settings(request, preferred_lang)
    base_url = "{0}/{1}".format(request.url_root[:request.url_root.find("/", 8)], current_lang)
    db_data = BlogPostHeader.query.filter(BlogPostHeader.url == post_url).one()
    post = BlogPost.populate_from_db(db_data, lang_fallback, base_url)

    db_data = BlogPostHeader.query.filter(BlogPostHeader.visible).order_by(BlogPostHeader.created_at.desc()).limit(2)
    recent_posts = [BlogPost.populate_from_db(d, lang_fallback, base_url) for d in db_data]
    return render_template("front/test_blogpost.html", v={
        "post": post,
        "recent_posts": recent_posts
    })


@front_bp.route("/contact")
def contact():
    current_lang, lang_fallback = langService.get_user_settings(request)
    db_data = BlogPostHeader.query.filter(BlogPostHeader.visible).order_by(BlogPostHeader.created_at.desc()).limit(2)
    base_url = "{0}/{1}".format(request.url_root[:request.url_root.find("/", 8)], current_lang)
    posts = [BlogPost.populate_from_db(d, lang_fallback, base_url) for d in db_data]

    return render_template("front/contact.html", v={
        "recent_posts": posts
    })


@login_required
@roles_required("root")
@front_bp.route("/data")
def data():
    db.drop_all()
    db.create_all()
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    from flask_security.utils import encrypt_password
    role = user_datastore.create_role(name="root", description="Site administrator")
    user_datastore.create_user(email='root@site.com', password=encrypt_password('pwd'), roles=[role])
    user_datastore.create_user(email='user@site.com', password=encrypt_password('pwd'))
    db.session.commit()
    return "OK"

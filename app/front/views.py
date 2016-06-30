# -*- coding: utf-8 -*-
import os

from flask import render_template, request, url_for, current_app, send_from_directory

from app.data.blog_posts import BlogPostHeader
from app.domain.language import Language
from app.services.language_service import langService
from . import front as front_bp
from flask.ext.security import SQLAlchemyUserDatastore
from app import db, User, Role
from flask.ext.login import login_required
from flask.ext.security import roles_required
from app.domain.blog_posts import BlogPost
from configs import Config as cfg



@front_bp.route("/")
def index():
    current_lang, lang_fallback = langService.get_user_settings(request)
    db_data = BlogPostHeader.query.filter(BlogPostHeader.visible).order_by(BlogPostHeader.published_at.desc()).limit(10)
    base_url = "{0}/{1}".format(request.url_root[:request.url_root.find("/", 8)], current_lang)
    posts = [BlogPost.populate_from_db(d, lang_fallback, base_url) for d in db_data]
    recent_posts = posts[:2]

    return render_template("front/index.html", v={
        "meta_language": Language.meta_lang[current_lang],
        "current_lang": current_lang,
        "posts": posts,
        "recent_posts": recent_posts
    })


@front_bp.route("/<string:lang_override>/<path:post_url>")
def detail(lang_override, post_url):
    current_lang, lang_fallback = langService.get_user_settings(request, lang_override)
    base_url = "{0}/{1}".format(request.url_root[:request.url_root.find("/", 8)], current_lang)
    db_data = BlogPostHeader.query.filter(BlogPostHeader.url == post_url).one()
    post = BlogPost.populate_from_db(db_data, lang_fallback, base_url)

    db_data = BlogPostHeader.query.filter(BlogPostHeader.visible).order_by(BlogPostHeader.created_at.desc()).limit(2)
    recent_posts = [BlogPost.populate_from_db(d, lang_fallback, base_url) for d in db_data]
    links = {lang: url_for(".detail", lang_override=lang, post_url=post_url) for lang in cfg.SUPPORTED_LANGS}
    html = render_template("front/blogpost.html", v={
        "lang_dic": {u"ru": u"Русский", u"en": u"English"},
        "links": links,
        "current_lang": current_lang,
        "meta_language": Language.meta_lang[current_lang],
        "post": post,
        "recent_posts": recent_posts
    })

    response = current_app.make_response(html)
    response.set_cookie('lang', value=current_lang)
    return response


@front_bp.route("/contact/")
def contact():
    current_lang, lang_fallback = langService.get_user_settings(request)
    db_data = BlogPostHeader.query.filter(BlogPostHeader.visible).order_by(BlogPostHeader.created_at.desc()).limit(2)
    base_url = "{0}/{1}".format(request.url_root[:request.url_root.find("/", 8)], current_lang)
    posts = [BlogPost.populate_from_db(d, lang_fallback, base_url) for d in db_data]
    if current_lang == "ru":
        tpl = "front/contact.ru.html"
    else:
        tpl = "front/contact.en.html"
    return render_template(tpl, v={
        "current_lang": current_lang,
        "meta_language": Language.meta_lang[current_lang],
        "recent_posts": posts
    })


@front_bp.route("/sitemap.xml")
def sitemap():
    return send_from_directory(os.path.join(cfg.APP_BASE_DIR, "static", "front"), "sitemap.xml")


@login_required
@roles_required("root")
@front_bp.route("/data")
def data():
    return
    db.drop_all()
    db.create_all()
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    from flask_security.utils import encrypt_password
    role = user_datastore.create_role(name="root", description="Site administrator")
    db.session.commit()
    return "OK"

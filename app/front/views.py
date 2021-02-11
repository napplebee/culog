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
from app.data.front.post import Post
from configs import Config as cfg
from app.common.constants import Constants as cnst
from app.common.phrases import PHRASES

import json
import random


@front_bp.route("/old/")
def index():
    current_lang, lang_fallback = langService.get_user_settings(request)
    db_data = BlogPostHeader.query.filter(BlogPostHeader.visible).order_by(BlogPostHeader.published_at.desc())
    # .limit(10)
    base_url = "{0}/{1}".format(request.url_root[:request.url_root.find("/", 8)], current_lang)
    posts = [post for post in [BlogPost.populate_from_db(d, lang_fallback, base_url) for d in db_data] if post.is_translated_for(current_lang)]

    recent_posts = posts[:2]

    return render_template("front/index.html", v={
        "meta_language": Language.meta_lang[current_lang],
        "current_lang": current_lang,
        "posts": posts,
        "recent_posts": recent_posts
    })



@front_bp.route("/old/<string:lang_override>/<path:post_url>")
def detail(lang_override, post_url):
    current_lang, lang_fallback = langService.get_user_settings(request, lang_override)
    base_url = "{0}/{1}".format(request.url_root[:request.url_root.find("/", 8)], current_lang)
    db_data = BlogPostHeader.query.filter(BlogPostHeader.url == post_url).one()
    post = BlogPost.populate_from_db(db_data, lang_fallback, base_url)

    db_data = BlogPostHeader.query.filter(BlogPostHeader.visible).order_by(BlogPostHeader.created_at.desc()).limit(2)
    recent_posts = [BlogPost.populate_from_db(d, lang_fallback, base_url) for d in db_data]
    links = {lang: url_for(".detail", lang_override=lang, post_url=post_url) for lang in cnst.SUPPORTED_LANGS}
    lang_dic = {u"ru": u"Русский", u"en": u"English"}
    filtered_lang_dic = {}
    for lang in lang_dic.keys():
        if post.is_translated_for(lang):
            filtered_lang_dic[lang] = lang_dic[lang]
    html = render_template("front/blogpost.html", v={
        "lang_dic": filtered_lang_dic,
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


@front_bp.route("/cookie-policy/")
def cookiepolicy():
    current_lang, lang_fallback = langService.get_user_settings(request)
    db_data = BlogPostHeader.query.filter(BlogPostHeader.visible).order_by(BlogPostHeader.created_at.desc()).limit(2)
    base_url = "{0}/{1}".format(request.url_root[:request.url_root.find("/", 8)], current_lang)
    posts = [BlogPost.populate_from_db(d, lang_fallback, base_url) for d in db_data]
    if current_lang == "ru":
        tpl = "front/cookie-policy.ru.html"
    else:
        tpl = "front/cookie-policy.en.html"
    return render_template(tpl, v={
        "current_lang": current_lang,
        "meta_language": Language.meta_lang[current_lang],
        "recent_posts": posts
    })


@front_bp.route("/sitemap.xml")
def sitemap():
    return send_from_directory(os.path.join(cfg.APP_BASE_DIR, "static", "front"), "sitemap.xml")


@front_bp.route("/robots.txt")
def robots():
    return send_from_directory(os.path.join(cfg.APP_BASE_DIR, "static", "front"), "robots.txt")


#region #### THE NEW WAY ####

@front_bp.route("/")
def nw_index():
    current_lang, lang_fallback = langService.get_user_settings(request)

    posts = Post.query.filter(Post.lang == current_lang)\
        .order_by(Post.published_at.desc(), Post.id.desc()).limit(cnst.ITEM_PER_PAGE + 1).all()

    # number of columns on landing page
    n = len(posts)
    has_next_item = n > cnst.ITEM_PER_PAGE
    if has_next_item:
        posts = posts[:-1]
        n = n - 1
    head = [*reversed(posts[:-(n % cnst.COLUMNS_ON_LANDING)])]
    tail = [*reversed(posts[-(n % cnst.COLUMNS_ON_LANDING):])]
    posts_left = []
    posts_center = []
    posts_right = []
    post_refs = [posts_left, posts_center, posts_right]

    while len(head) > 0:
        posts_left.append(head.pop())
        posts_center.append(head.pop())
        posts_right.append(head.pop())

    i = 0
    while len(tail) > 0:
        post_refs[i % cnst.COLUMNS_ON_LANDING].append(tail.pop())
        i += 1

    #TODO: replace with /
    links = {lang: "/" for lang in cnst.SUPPORTED_LANGS}
    lang_dic = {u"ru": u"Русский", u"en": u"English"}
    return render_template("front/post/index.html", v={
        "links": links,
        "lang_dic": lang_dic,
        "meta_language": Language.meta_lang[current_lang],
        "current_lang": current_lang,
        "posts_left": posts_left,
        "posts_center": posts_center,
        "posts_right": posts_right,
        "phrases": PHRASES[current_lang],
        "has_next_item": has_next_item
    })


@front_bp.route("/more/<int:page>", methods=["POST",])
def nw_index_more(page):
    current_lang, lang_fallback = langService.get_user_settings(request)

    posts = Post.query.filter(Post.lang == current_lang) \
        .order_by(Post.published_at.desc(), Post.id.desc()).offset(page*cnst.ITEM_PER_PAGE).limit(cnst.ITEM_PER_PAGE + 1).all()

    # number of columns on landing page
    n = len(posts)
    has_next_item = n > cnst.ITEM_PER_PAGE
    if has_next_item:
        posts = posts[:-1]
        n = n - 1
    head = [*reversed(posts[:-(n % cnst.COLUMNS_ON_LANDING)])]
    tail = [*reversed(posts[-(n % cnst.COLUMNS_ON_LANDING):])]
    posts_left = []
    posts_center = []
    posts_right = []
    post_refs = [posts_left, posts_center, posts_right]

    while len(head) > 0:
        posts_left.append(head.pop())
        posts_center.append(head.pop())
        posts_right.append(head.pop())

    i = 0
    while len(tail) > 0:
        post_refs[i % cnst.COLUMNS_ON_LANDING].append(tail.pop())
        i += 1

    # TODO: replace with /
    links = {lang: "/" for lang in cnst.SUPPORTED_LANGS}
    lang_dic = {u"ru": u"Русский", u"en": u"English"}

    html = render_template("front/post/recipe_more.html", v={
        "links": links,
        "lang_dic": lang_dic,
        "meta_language": Language.meta_lang[current_lang],
        "current_lang": current_lang,
        "posts_left": posts_left,
        "posts_center": posts_center,
        "posts_right": posts_right,
        "phrases": PHRASES[current_lang],

    })
    result = {
        "payload": html,
        "has_next_item": has_next_item
    }
    return json.dumps(result)


@front_bp.route("/<string:lang_override>/category/<string:category>")
def nw_category(lang_override, category):
    current_lang, lang_fallback = langService.get_user_settings(request, lang_override)

    search = "%{}%".format(category)
    posts = Post.query.filter(Post.lang == current_lang, Post.recipe_category.like(search)) \
        .order_by(Post.published_at.desc(), Post.id.desc()).limit(cnst.ITEM_PER_PAGE + 1).all()

    # number of columns on landing page
    n = len(posts)
    has_next_item = n > cnst.ITEM_PER_PAGE
    if has_next_item:
        posts = posts[:-1]
        n = n - 1
    head = [*reversed(posts[:-(n % cnst.COLUMNS_ON_LANDING)])]
    tail = [*reversed(posts[-(n % cnst.COLUMNS_ON_LANDING):])]
    posts_left = []
    posts_center = []
    posts_right = []
    post_refs = [posts_left, posts_center, posts_right]

    while len(head) > 0:
        posts_left.append(head.pop())
        posts_center.append(head.pop())
        posts_right.append(head.pop())

    i = 0
    while len(tail) > 0:
        post_refs[i % cnst.COLUMNS_ON_LANDING].append(tail.pop())
        i += 1

    # TODO: replace with /
    links = {lang: "/" for lang in cnst.SUPPORTED_LANGS}
    lang_dic = {u"ru": u"Русский", u"en": u"English"}
    return render_template("front/post/index.html", v={
        "links": links,
        "lang_dic": lang_dic,
        "meta_language": Language.meta_lang[current_lang],
        "current_lang": current_lang,
        "posts_left": posts_left,
        "posts_center": posts_center,
        "posts_right": posts_right,
        "phrases": PHRASES[current_lang],
        "has_next_item": has_next_item
    })


@front_bp.route("/<string:lang_override>/category/<string:category>/more")
def nw_category_more(lang_override, category):
    return "%s -- %s" % (lang_override, category)


@front_bp.route("/<string:lang_override>/<path:post_url>")
def nw_detail(lang_override, post_url):
    current_lang, lang_fallback = langService.get_user_settings(request, lang_override)
    url = Post.makeup_url(post_url)
    posts = Post.query.filter(Post.url == url).all()

    post = None
    for p in posts:
        if p.lang == current_lang:
            post = p
            break

    if post is None:
        # TODO: raise 404
        raise ValueError("Not found")

    available_translations = [_.lang for _ in posts]

    links = {lang: url_for(".nw_detail", lang_override=lang, post_url=post_url) for lang in cnst.SUPPORTED_LANGS}

    lang_dic = {u"ru": u"Русский", u"en": u"English"}
    filtered_lang_dic = {}
    for lang in lang_dic.keys():
        if lang in available_translations:
            filtered_lang_dic[lang] = lang_dic[lang]

    category = post.recipe_category.split(",")[0]

    search = "%{}%".format(category)
    might_like_posts = set(Post.query.filter(Post.recipe_category.like(search)).limit(12).all())

    recent_posts = Post.query.filter(Post.lang == current_lang).\
        order_by(Post.published_at.desc(), Post.id.asc()).limit(6).all()

    might_like_posts = might_like_posts - set(recent_posts)
    might_like_posts = random.sample(might_like_posts, min(2, len(might_like_posts)))

    if len(might_like_posts) == 0:
        might_like_posts = recent_posts[-3:]

    uniq_category = []
    for c, *_ in Post.query.filter(Post.lang == current_lang).with_entities(Post.recipe_category).all():
        uniq_category.extend(_.strip() for _ in c.split(",") if _.strip() != "")
    categories = [
        (c, url_for(".nw_category", lang_override=current_lang, category=c)) for c in set(uniq_category)
    ]

    html = render_template("front/post/detail.html", v={
        "lang_dic": filtered_lang_dic,
        "links": links,
        "current_lang": current_lang,
        "post": post,
        "recent_posts": recent_posts[0:3],
        "might_like_posts": might_like_posts,
        "categories": categories,
        "phrases": PHRASES[current_lang],
        "meta_language": Language.meta_lang[current_lang],
    })
    response = current_app.make_response(html)
    response.set_cookie('lang', value=current_lang)
    return response


#endregion


@front_bp.route("/migrate")
def migrate():
    if True:
        pass
    else:
        for current_lang, lang_fallback in [("en", ["en"]), ("ru", ["ru", "en"]), ]:

            db_data = BlogPostHeader.query.filter(BlogPostHeader.visible).order_by(BlogPostHeader.published_at.desc())
            # .limit(10)
            base_url = "{0}/{1}".format(request.url_root[:request.url_root.find("/", 8)], current_lang)
            posts = [post for post in [BlogPost.populate_from_db(d, lang_fallback, base_url) for d in db_data] if
                     post.is_translated_for(current_lang)]

            for oldPost in posts:
                newPost = Post()
                newPost.url = Post.makeup_url(oldPost.url)
                newPost.lang = current_lang
                newPost.visible = oldPost.visible

                newPost.title = oldPost.get_title()
                newPost.sub_title = oldPost.get_sub_title()

                newPost.recipe_yield = oldPost.get_recipe_yield()
                newPost.recipe_cuisine = oldPost.get_recipe_cuisine()
                newPost.recipe_category = oldPost.get_recipe_category()

                newPost.published_at = oldPost.published_at
                newPost.updated_at = oldPost.updated_at

                newPost.fb_likes = oldPost.fb_likes
                newPost.fb_og_image = oldPost.og_image
                newPost.fb_og_title = oldPost.get_og_title()
                newPost.fb_og_description = oldPost.get_og_description()

                newPost.meta_keywords = oldPost.get_keywords()
                newPost.meta_description = oldPost.get_description()

                newPost.cook_time = oldPost.cook_time
                newPost.prep_time = oldPost.prep_time

                newPost.total_fats = None
                newPost.total_carbs = None
                newPost.total_proteins = None

                newPost.recipe_id = -1

                newPost.cut = oldPost.get_cut()
                newPost.text = oldPost.get_text()

                db.session.add(newPost)

            db.session.commit()

    return "OK"


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

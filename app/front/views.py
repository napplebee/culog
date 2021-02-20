# -*- coding: utf-8 -*-
import os

from flask import render_template, request, url_for, current_app, send_from_directory

from app.data.blog_posts import BlogPostHeader
from app.domain.language import Language
from app.services.language_service import langService
from . import front as front_bp
from app.data.front.post import Post
from configs import Config as cfg
from app.common.constants import Constants as cnst
from app.common.phrases import PHRASES

import json
import random


@front_bp.route("/cookie-policy/")
def cookiepolicy():
    current_lang, lang_fallback = langService.get_user_settings(request)
    uniq_category = []
    for c in Post.query.filter(Post.lang == current_lang).with_entities(Post.recipe_category).all():
        uniq_category.extend(_.strip() for _ in c[0].split(",") if _.strip() != "")
    categories = [
        (c, url_for(".nw_category", lang_override=current_lang, category=c)) for c in set(uniq_category)
    ]
    recent_posts = Post.query.filter(Post.lang == current_lang, Post.fb_og_image != ''). \
        order_by(Post.published_at.desc(), Post.id.asc()).limit(6).all()

    if current_lang == "ru":
        tpl = "front/post/cookie-policy.ru.html"
    else:
        tpl = "front/post/cookie-policy.en.html"
    return render_template(tpl, v={
        "current_lang": current_lang,
        "meta_language": Language.meta_lang[current_lang],
        "phrases": PHRASES[current_lang],
        "lang_dic": {u"ru": u"Русский", u"en": u"English"},
        "categories": categories,
        "links": {lang: url_for(".cookiepolicy") for lang in cnst.SUPPORTED_LANGS},
        "recent_posts": recent_posts[0:3],
        "might_like_posts": recent_posts[-3:]
    })


@front_bp.route("/sitemap.xml")
def sitemap():
    return send_from_directory(os.path.join(cfg.APP_BASE_DIR, "static", "front"), "sitemap.xml")


@front_bp.route("/robots.txt")
def robots():
    return send_from_directory(os.path.join(cfg.APP_BASE_DIR, "static", "front"), "robots.txt")


@front_bp.route("/")
def nw_index():
    current_lang, lang_fallback = langService.get_user_settings(request)

    posts = Post.query.filter(Post.lang == current_lang, Post.visible == True)\
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

    posts = Post.query.filter(Post.lang == current_lang, Post.visible == True) \
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
    posts = Post.query.filter(Post.lang == current_lang, Post.visible == True, Post.recipe_category.like(search)) \
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


@front_bp.route("/more/<string:lang_override>/category/<string:category>/<int:page>", methods=["POST",])
def nw_category_more(lang_override, category, page):
    current_lang, lang_fallback = langService.get_user_settings(request, lang_override)

    search = "%{}%".format(category)
    posts = Post.query.filter(Post.lang == current_lang, Post.visible == True, Post.recipe_category.like(search)) \
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


@front_bp.route("/<string:lang_override>/<path:post_url>")
def nw_detail(lang_override, post_url):
    current_lang, lang_fallback = langService.get_user_settings(request, lang_override)
    url = Post.makeup_url(post_url)
    posts = Post.query.filter(Post.url == url, Post.visible == True).all()

    post = None
    for p in posts:
        if p.lang == current_lang:
            post = p
            break

    if post is None:
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
    might_like_posts = set(Post.query.filter(Post.id != post.id, Post.visible == True, Post.fb_og_image != '', Post.recipe_category.like(search)).limit(12).all())

    recent_posts = Post.query.filter(Post.id != post.id, Post.visible == True, Post.lang == current_lang, Post.fb_og_image != '').\
        order_by(Post.published_at.desc(), Post.id.asc()).limit(6).all()

    might_like_posts = might_like_posts - set(recent_posts)
    might_like_posts = random.sample(might_like_posts, min(2, len(might_like_posts)))

    if len(might_like_posts) == 0:
        might_like_posts = recent_posts[-3:]

    uniq_category = []
    for c in Post.query.filter(Post.lang == current_lang, Post.visible == True).with_entities(Post.recipe_category).all():
        uniq_category.extend(_.strip() for _ in c[0].split(",") if _.strip() != "")
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


@front_bp.route("/<string:lang_override>/about")
def about(lang_override):
    current_lang, lang_fallback = langService.get_user_settings(request, lang_override)
    lang_dic = {u"ru": u"Русский", u"en": u"English"}
    links = {lang: url_for(".about", lang_override=lang) for lang in cnst.SUPPORTED_LANGS}
    return render_template("front/about.%s.html" % current_lang, v={
        "links": links,
        "lang_dic": lang_dic,
        "meta_language": Language.meta_lang[current_lang],
        "current_lang": current_lang,
        "phrases": PHRASES[current_lang],
    })

#endregion
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
from operator import itemgetter
import logging

from app.data.admin.recipe import RecipeHeaderEn, RecipeHeaderRu


import json
import random

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s',)
logger = logging.getLogger(__name__)
@front_bp.route("/ads.txt")
def ads():
    tpl = "front/ads.txt"
    return render_template(tpl)

@front_bp.route("/cookie-policy/")
def cookiepolicy():
    current_lang, lang_fallback = langService.get_user_settings(request)
    uniq_category = []
    for c in Post.query.filter(Post.lang == current_lang, Post.visible == True).with_entities(Post.recipe_category).all():
        uniq_category.extend(_.strip() for _ in c[0].split(",") if _.strip() != "")
    categories = [
        (c, url_for(".nw_category", lang_override=current_lang, category=c.replace(" ", "_"))) for c in set(uniq_category)
    ]
    categories = sorted(categories, key=itemgetter(0))

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

    uniq_category = []
    for c in Post.query.filter(Post.lang == current_lang, Post.visible == True).with_entities(Post.recipe_category).all():
        uniq_category.extend(_.strip() for _ in c[0].split(",") if _.strip() != "")
    categories = [
        (c, url_for(".nw_category", lang_override=current_lang, category=c.replace(" ", "_"))) for c in set(uniq_category)
    ]
    categories = sorted(categories, key=itemgetter(0))

    posts = Post.query.filter(Post.lang == current_lang, Post.visible == True)\
        .order_by(Post.published_at.desc(), Post.id.desc()).limit(cnst.ITEM_PER_PAGE + 1).all()

    # number of columns on landing page
    n = len(posts)
    has_next_item = n > cnst.ITEM_PER_PAGE
    if has_next_item:
        posts = posts[:-1]
        n = n - 1
    head = [_ for _ in reversed(posts[:-(n % cnst.COLUMNS_ON_LANDING)])]
    tail = [_ for _ in reversed(posts[-(n % cnst.COLUMNS_ON_LANDING):])]
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
        "has_next_item": has_next_item,
        "categories": categories
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
    head = [_ for _ in reversed(posts[:-(n % cnst.COLUMNS_ON_LANDING)])]
    tail = [_ for _ in reversed(posts[-(n % cnst.COLUMNS_ON_LANDING):])]
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

    search = "%%%s%%" % category
    posts = Post.query.filter(Post.lang == current_lang, Post.visible == True, Post.recipe_category.like(search)) \
        .order_by(Post.published_at.desc(), Post.id.desc()).limit(cnst.ITEM_PER_PAGE + 1).all()

    uniq_category = []
    for c in Post.query.filter(Post.lang == current_lang, Post.visible == True).with_entities(Post.recipe_category).all():
        uniq_category.extend(_.strip() for _ in c[0].split(",") if _.strip() != "")
    categories = [
        (c, url_for(".nw_category", lang_override=current_lang, category=c.replace(" ", "_"))) for c in set(uniq_category)
    ]
    categories = sorted(categories, key=itemgetter(0))

    # number of columns on landing page
    n = len(posts)
    has_next_item = n > cnst.ITEM_PER_PAGE
    if has_next_item:
        posts = posts[:-1]
        n = n - 1
    head = [_ for _ in reversed(posts[:-(n % cnst.COLUMNS_ON_LANDING)])]
    tail = [_ for _ in reversed(posts[-(n % cnst.COLUMNS_ON_LANDING):])]
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
        "has_next_item": has_next_item,
        "categories": categories,
        "category": category.replace("_", " ")
    })


@front_bp.route("/more/<string:lang_override>/category/<string:category>/<int:page>", methods=["POST",])
def nw_category_more(lang_override, category, page):
    current_lang, lang_fallback = langService.get_user_settings(request, lang_override)

    search = "%%%s%%" % category
    posts = Post.query.filter(Post.lang == current_lang, Post.visible == True, Post.recipe_category.like(search)) \
        .order_by(Post.published_at.desc(), Post.id.desc()).offset(page*cnst.ITEM_PER_PAGE).limit(cnst.ITEM_PER_PAGE + 1).all()

    # number of columns on landing page
    n = len(posts)
    has_next_item = n > cnst.ITEM_PER_PAGE
    if has_next_item:
        posts = posts[:-1]
        n = n - 1
    head = [_ for _ in reversed(posts[:-(n % cnst.COLUMNS_ON_LANDING)])]
    tail = [_ for _ in reversed(posts[-(n % cnst.COLUMNS_ON_LANDING):])]
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

    search = "%%%s%%" % category
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
        (c, url_for(".nw_category", lang_override=current_lang, category=c.replace(" ", "_"))) for c in set(uniq_category)
    ]
    categories = sorted(categories, key=itemgetter(0))

    # dirty hack, gotta be part of cooking the recipe
    # the whole ld_json thing deserves to be an entity
    def get_ld_json_ingredients():
        if post.recipe_id == -1:
            return []
        _ = []
        if not post.is_article:
            recipe_header = None
            amount_types = PHRASES[current_lang].amount_types
            if current_lang == "ru":
                recipe_header = RecipeHeaderRu.query.filter(RecipeHeaderRu.recipe_id == post.recipe_id).one()
            elif current_lang == "en":
                recipe_header = RecipeHeaderEn.query.filter(RecipeHeaderEn.recipe_id == post.recipe_id).one()
            else:
                raise ValueError("Unknown language")

            for i_type in recipe_header.ingredients_type:
                if len(i_type.ingredients) > 0:
                    for ingr in i_type.ingredients:
                        amount_str = ""
                        if ingr.amount_value is not None and ingr.amount_value != "":
                            amount_str = "{} {}".format(ingr.amount_value, amount_types[ingr.amount_type]).strip()
                        ingr_str = "{} {}".format(amount_str, ingr.name).lstrip().rstrip(".,")
                        _.append("\"" + ingr_str.lower() + "\"")

        return _

    ld_json_ingredients = get_ld_json_ingredients()

    html = render_template("front/post/detail.html", v={
        "ld_json_ingredients": ",".join(ld_json_ingredients),
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
    uniq_category = []
    for c in Post.query.filter(Post.lang == current_lang, Post.visible == True).with_entities(Post.recipe_category).all():
        uniq_category.extend(_.strip() for _ in c[0].split(",") if _.strip() != "")
    categories = [
        (c, url_for(".nw_category", lang_override=current_lang, category=c.replace(" ", "_"))) for c in set(uniq_category)
    ]
    categories = sorted(categories, key=itemgetter(0))

    return render_template("front/about.%s.html" % current_lang, v={
        "links": links,
        "lang_dic": lang_dic,
        "meta_language": Language.meta_lang[current_lang],
        "current_lang": current_lang,
        "phrases": PHRASES[current_lang],
        "categories": categories
    })

#endregion

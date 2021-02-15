# -*- coding: utf-8 -*-

from app.data.blog_posts import BlogPostHeader
from app.domain.blog_posts import BlogPost
from . import admin

from flask.ext.login import login_required
from flask.ext.security import roles_required
from flask import render_template, request, url_for, redirect
from app.services.language_service import langService
from app.common.constants import Constants as cnst

from app import db
from app.admin.forms import PostForm
from app.admin import forms as nf
from app.data.admin.recipe import Recipe
from app.data.front.post import Post

import json


@admin.route("/")
@login_required
@roles_required("root")
def index():
    return render_template("admin/base.html")


@admin.route("/post/all")
@login_required
@roles_required("root")
def post_list():
    posts = [
        {
            "id": p.id,
            "title": p.title,
            "recipe_id" : p.recipe_id,
            "lang": p.lang,
            "published_at": p.published_at.strftime('%d.%m.%y %H:%M') if p.published_at else "",
            "updated_at": p.updated_at.strftime('%d.%m.%y %H:%M') if p.updated_at else "",
            "visible": p.visible
        } for p in Post.query.order_by(Post.updated_at.desc(), Post.id.desc()).all()
    ]
    return render_template("admin/post/list.html", v={
        "posts": posts,
        "supported_langs": cnst.SUPPORTED_LANGS
        })


# @admin.route("/blog/new", methods=["POST", "GET"])
# @login_required
# @roles_required("root")
# def blog_post_new():
#     f = BlogPostForm()
#     # if request.method == "POST" and f.validate():
#     if request.method == "POST":
#         post = BlogPost.populate_from_ui(f)
#         post_id = post.save()
#         return redirect("/admin/blog/update/{0}?saved".format(post_id))
#     title = "Create new post"
#     return render_template("admin/blog/detail.html", v={
#         "title": title,
#         "f": f,
#         "action": ""
#     })


@admin.route("/post/update/<int:post_id>", methods=["POST", "GET"])
@login_required
@roles_required("root")
def post_update(post_id):
    if request.method == "POST":
        f = PostForm()
        post = Post.query.get(post_id)
        post.hotfix(f)
        # post = Post.populate_from_ui(f)
        # post.update()
        return redirect("/admin/post/update/{0}?saved".format(post_id))
        # return redirect(url_for('.blog_post_list'))
    else:
        post = Post.query.get(post_id)
        # post = BlogPost.populate_from_db(BlogPostHeader.query.get(post_id))
        f = PostForm(obj=post)

        return render_template("admin/post/update.html", v={
            "title": post.title,
            "f": f,
            "action": "",
            "saved": 1 if "saved" in request.args else 0
        })


# @login_required
# @roles_required("root")
# @admin.route("/post_preview/<string:lang_override>/<int:post_id>")
# def blog_post_preview(lang_override, post_id):
#     current_lang, lang_fallback = langService.get_user_settings(request, lang_override)
#     base_url = "{0}/{1}".format(lang_override, request.url_root[:request.url_root.find("/", 8)])
#     db_data = BlogPostHeader.query.get(post_id)
#     post = BlogPost.populate_from_db(db_data, lang_fallback, base_url)
#     return render_template("admin/blog/preview.html", v={
#         "post": post
#     })


# @login_required
# @roles_required("root")
# @admin.route("/post_list_preview/<string:lang_override>")
# def blog_list_preview(lang_override):
#     current_lang, lang_fallback = langService.get_user_settings(request, lang_override)
#     db_data = BlogPostHeader.query.filter().order_by(BlogPostHeader.created_at.desc())
#     base_url = "{0}/{1}".format(request.url_root[:request.url_root.find("/", 8)], current_lang)
#     posts = [BlogPost.populate_from_db(d, lang_fallback, base_url) for d in db_data]
#     return render_template("admin/blog/list_preview.html", v={
#         "posts": posts
#     })


@login_required
@roles_required("root")
@admin.route("/test/create", methods=["GET"])
def fck():
    # return "Ok"
    from app.core import db
    db.create_all()
    return "Ok"


@admin.route("/migrate")
def migrate():
    if True:
        pass
    else:
        for current_lang, lang_fallback in [("en", ["en"]), ("ru", ["ru", "en"]), ]:

            db_data = BlogPostHeader.query.filter(BlogPostHeader.visible).order_by(
                BlogPostHeader.published_at.desc())
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

                if oldPost.published_at is not None:
                    newPost.published_at = oldPost.published_at
                else:
                    newPost.published_at = dt.datetime.utcnow()

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
@admin.route("/recipe/all", methods=["GET", ])
def recipe_all():

    recipes = Recipe.query.order_by(Recipe.updated_at.desc(), Recipe.created_at.desc()).all()
    return render_template("admin/recipe/list.html", v={
        "recipes": recipes,
        "supported_langs": cnst.SUPPORTED_LANGS
    })


@login_required
@roles_required("root")
@admin.route("/recipe/new", methods=["POST", "GET"])
def recipe_new():
    form = nf.RecipeForm()

    if request.method == "POST":
        post = Recipe.populate_from_ui(form)
        post_id = post.save()
        return redirect("/admin/recipe/update/{0}?saved".format(post_id))

    return render_template("admin/recipe/detail.html", v={
        "f": form,
        "action": ""
    })


@admin.route("/recipe/update/<int:recipe_id>", methods=["POST", "GET"])
@login_required
@roles_required("root")
def recipe_update(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if request.method == "POST":
        form = nf.RecipeForm()
        recipe.update(form)
        return redirect("/admin/recipe/update/{0}?saved".format(recipe_id))
    else:
        title = u"Updating {0}".format(recipe.name)
        form = nf.RecipeForm()
        form.process(obj=recipe)

        return render_template("admin/recipe/detail.html", v={
            "title": title,
            "f": form,
            "action": "",
            "saved": 1 if "saved" in request.args else 0,
            "rendered": 1 if "rendered" in request.args else 0
        })


@admin.route("/recipe/render/<int:recipe_id>/<string:lang>", methods=["POST"])
@login_required
@roles_required("root")
def recipe_render(recipe_id, lang):
    if lang == cnst.ALL_LANG:
        langs = [cnst.RU_LANG, cnst.EN_LANG, ]
    elif lang == cnst.RU_LANG:
        langs = [cnst.RU_LANG, ]
    elif lang == cnst.EN_LANG:
        langs = [cnst.EN_LANG, ]
    else:
        raise ValueError("unknown lang code")

    recipe = Recipe.query.get(recipe_id)
    r = Post.cook_from(recipe, langs)
    result = []
    for k, v in r.items():
        result.append({"recipe_id": v.id, 'lang': k})
    return json.dumps(result)


@admin.route("/recipe/visibility", methods=["POST"])
@login_required
@roles_required("root")
def recipe_visibility():
    try:
        recipe_id = int(request.form["recipe_id"])
        lang = request.form["lang"]
        visibility = request.form["visibility"].upper() == "TRUE"
        p = Post.query.filter(Post.recipe_id == recipe_id, Post.lang == lang).one()
        if visibility:
            p.make_visible()
        else:
            p.make_invisible()

        message = "%s post for recipe (%s) is %s now" % (
            lang.upper(), recipe_id, "visible" if visibility else "invisible")
    except Exception as error:
        message = error

    result = {"message": message}
    return json.dumps(result)


@admin.route("/recipe/preview-list/<string:lang>", methods=["GET"])
@login_required
@roles_required("root")
def recipe_list_preview(lang):
    pass


@admin.route("/recipe/preview/<int:recipe_id>/<string:lang>", methods=["POST", "GET"])
@login_required
@roles_required("root")
def single_recipe_preview(recipe_id, lang):
    pass

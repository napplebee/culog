# -*- coding: utf-8 -*-

from app.data.blog_posts import BlogPostHeader
from app.domain.blog_posts import BlogPost
from . import admin

from flask.ext.login import login_required
from flask.ext.security import roles_required
from flask import render_template, request, url_for, redirect
from app.services.language_service import langService
from configs import Config as cfg

from app.admin.forms import BlogPostForm
from app.admin import new_forms as nf
from app.data.admin.recipe import Recipe


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
@admin.route("/test/create", methods=["GET"])
def fck():
    from app.core import db
    db.create_all()
    print("Ok")

#region cookwithlove 2.0

@login_required
@roles_required("root")
@admin.route("/recipe/all", methods=["GET", ])
def recipe_all():

    recipes = Recipe.query.order_by(Recipe.updated_at.desc(), Recipe.created_at.desc()).all()
    return render_template("admin/recipe/list.html", v={
        "recipes": recipes,
        "supported_langs": cfg.SUPPORTED_LANGS
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
    else:
        pass

    return render_template("admin/recipe/detail.html", v={
        "f": form,
        "action": ""
    })


@admin.route("/recipe/update/<int:recipe_id>", methods=["POST", "GET"])
@login_required
@roles_required("root")
def recipe_update(recipe_id):
    if request.method == "POST":
        form = nf.RecipeForm()
        post = Recipe.populate_from_ui(form)
        post.update()
        return redirect("/admin/recipe/update/{0}?saved".format(recipe_id))
    else:
        recipe = Recipe.query.get(recipe_id)

        title = u"Update {0}".format(recipe.name)

        ru_recipe_header_form = nf.RecipeHeaderForm(obj=recipe.recipe_header_ru)
        en_recipe_header_form = nf.RecipeHeaderForm(obj=recipe.recipe_header_en)

        l = list(recipe.recipe_header_ru.ingredient_types_ru)
        l = [ _ for _ in recipe.recipe_header_ru.ingredient_types_ru ]
        # ru_recipe_header_form.ingredients_type.process([])
        # for ingr_type in recipe.recipe_header_ru.ingredient_types_ru:
        #     ingr_type_form = nf.IngredientTypeForm(obj=ingr_type)
        #
        #     for ing in ingr_type.ingredients_ru:
        #         ingr_form = nf.IngredientForm(obj=ing)
        #         ingr_type_form.ingredients.append_entry(ing)
        #     ru_recipe_header_form.ingredients_type.append_entry(ingr_type)

        for ingr_type in recipe.recipe_header_en.ingredient_types_en:
            ingr_type_form = nf.IngredientTypeForm(obj=ingr_type)

            for ing in ingr_type.ingredients_en:
                ingr_form = nf.IngredientForm(obj=ing)
                ingr_type_form.ingredients.append_entry(ingr_form)

            en_recipe_header_form.ingredients_type.append_entry(ingr_type_form)

        form = nf.RecipeForm()
        form.process(obj=recipe)
        # for fuck's sake
        form_recipe_header_ru = form.recipe_header_ru.form
        form_recipe_header_en = form.recipe_header_en.form
        form_recipe_header_ru.ingredients_type.pop_entry()
        form_recipe_header_en.ingredients_type.pop_entry()

        for ingr_type in recipe.recipe_header_ru.ingredient_types_ru:
            len(ingr_type.ingredients_ru)
            form_recipe_header_ru.ingredients_type.append_entry(ingr_type)

            # form_recipe_header_ru.ingredients_type



        # form.recipe_header_ru.form.process(obj=ru_recipe_header_form)
        # form.recipe_header_en.form.process(obj=en_recipe_header_form)

        return render_template("admin/recipe/detail.html", v={
            "title": title,
            "f": form,
            "action": "",
            "saved": 1 if "saved" in request.args else 0
        })


@admin.route("/recipe/preview-list/<string:lang>", methods=["GET"])
@login_required
@roles_required("root")
def recipe_list_preview(lang):
    pass


@admin.route("/recipe/preview/<int:recipe_id>>/<string:lang>", methods=["POST", "GET"])
@login_required
@roles_required("root")
def single_recipe_preview(recipe_id, lang):
    pass

#endregion cookwithlove 2.0
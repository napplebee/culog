# -*- coding: utf-8 -*-

from app.core import db
from app.common.constants import Constants as cnst
from app.common.phrases import PHRASES
import datetime as dt


class Post(db.Model):
    __tablename__ = 'ng_posts'

    id = db.Column(db.Integer, primary_key=True, )
    url = db.Column(db.String)
    lang = db.Column(db.String)
    visible = db.Column(db.Boolean, default=False)

    title = db.Column(db.String)
    sub_title = db.Column(db.String)

    recipe_yield = db.Column(db.String)
    recipe_cuisine = db.Column(db.String)
    recipe_category = db.Column(db.String)

    published_at = db.Column(db.DateTime, default=dt.datetime.utcnow)
    updated_at = db.Column(db.DateTime)

    fb_likes = db.Column(db.Integer, default=0)
    fb_og_image = db.Column(db.String)
    fb_og_title = db.Column(db.String)
    fb_og_description = db.Column(db.String)

    meta_keywords = db.Column(db.String)
    meta_description = db.Column(db.String)

    cook_time = db.Column(db.String)
    prep_time = db.Column(db.String)

    total_fats = db.Column(db.Numeric)
    total_carbs = db.Column(db.Numeric)
    total_proteins = db.Column(db.Numeric)

    cut = db.Column(db.Text)
    text = db.Column(db.Text)

    recipe_id = db.Column(db.Integer)

    @staticmethod
    def cook_from(recipe, langs):
        posts = Post.query.filter(Post.recipe_id == recipe.id).all()
        result = {}

        for lang in langs:
            _post = None

            def add_to_session(_):
                db.session.merge(_)

            for p in posts:
                if p.lang == lang:
                    _post = p
                    break
            # Idiot-proof
            # by design: if all posts were found, then all langs must be present.
            # Hence, "_post is None" must be raised as error
            if len(posts) == len(cnst.SUPPORTED_LANGS) and _post is None:
                raise ValueError("All posts for recipe (%s) were found but there is no post for '%s' language" % (
                    recipe.id, lang
                ))

            if _post is None:
                _post = Post()

                def add_to_session(_):
                    db.session.add(_)

            header_field = "recipe_header_%s" % lang
            if not hasattr(recipe, header_field):
                raise ValueError("Recipe (%s) doesn't have '%s' attribute" % (recipe.id, header_field))

            _post.__cook(lang, getattr(recipe, header_field), recipe)
            add_to_session(_post)
            result[lang] = _post

        db.session.commit()

        return result

    @staticmethod
    def makeup_url(url):
        if not url.startswith("/"):
            url = "/%s" % url
        if url.endswith("/"):
            url = url[:-1]
        return url

    def __cook(self, _lang, _header, _recipe):
        self.lang = _lang
        self.url = Post.makeup_url(_recipe.url)
        self.recipe_id = _recipe.id

        self.title = _header.title
        self.sub_title = _header.sub_title

        self.recipe_yield = _header.recipe_yield
        self.recipe_cuisine = _header.recipe_cuisine
        self.recipe_category = _header.recipe_category

        self.cook_time = _recipe.cook_time
        self.prep_time = _recipe.prep_time

        self.total_fats = _recipe.total_fats
        self.total_carbs = _recipe.total_carbs
        self.total_proteins = _recipe.total_proteins

        self.published_at = _recipe.published_at if _recipe.published_at is not None else dt.datetime.utcnow()
        self.updated_at = dt.datetime.utcnow()

        self.fb_og_title = _header.fb_og_title
        self.fb_og_description = _header.fb_og_description
        self.fb_og_image = _recipe.fb_og_image

        self.meta_keywords = _header.meta_keywords
        self.meta_description = _header.meta_description

        self.cut = _header.cut
        self.render(_recipe, _header, _lang)

    def render(self, recipe, head, lang):
        import jinja2
        from configs import basedir
        import os

        templateLoader = jinja2.FileSystemLoader(
            searchpath=os.path.join(basedir, "app", "templates")
        )
        templateEnv = jinja2.Environment(loader=templateLoader)
        template = templateEnv.get_template("admin/recipe/render.html")
        _text = template.render(v={
            "r": recipe,
            "h": head,
            "ph": PHRASES[lang]
        })

        self.text = _text

    def make_visible(self):
        self.visible = True
        db.session.commit()

    def make_invisible(self):
        self.visible = False
        db.session.commit()

    def get_categories(self):
        return [_.strip() for _ in self.recipe_category.split(",") if _ != ""]

    def hotfix(self, form):
        if self.id != int(form.id.data):
            raise ValueError("Wrong id %s - %s", self.id, form.id.data)

        self.url = Post.makeup_url(form.url.data)
        self.lang = form.lang.data
        self.visible = form.visible.data
        self.title = form.title.data
        self.sub_title = form.sub_title.data
        self.recipe_yield = form.recipe_yield.data
        self.recipe_cuisine = form.recipe_cuisine.data
        self.recipe_category = form.recipe_category.data
        self.published_at = form.published_at.data
        self.fb_likes = int(form.fb_likes.data)
        self.fb_og_image = form.fb_og_image.data
        self.fb_og_title = form.fb_og_title.data
        self.fb_og_description = form.fb_og_description.data
        self.meta_keywords = form.meta_keywords.data
        self.meta_description = form.meta_description.data
        self.cook_time = form.cook_time.data
        self.prep_time = form.prep_time.data
        self.total_fats = float(form.total_fats.data if len(form.total_fats.data) > 0 else 0)
        self.total_carbs = float(form.total_carbs.data if form.total_carbs.data != "" else 0)
        self.total_proteins = float(form.total_proteins.data if form.total_proteins.data != "" else 0)
        self.cut = form.cut.data
        self.text = form.text.data

        db.session.commit()

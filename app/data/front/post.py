# -*- coding: utf-8 -*-

from app.core import db
from app.common.constants import Constants as cnst

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

    published_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    fb_og_image = db.Column(db.String)
    fb_og_title = db.Column(db.String)
    fb_og_description = db.Column(db.String)

    meta_keywords = db.Column(db.String)
    meta_description = db.Column(db.String)

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
    def __makeup_url(lang, url):
        if not url.startswith("/"):
            url = "/%s" % url
        if not url.endswith("/"):
            url = "%s/" % url
        return "%s%s" % (lang, url)

    def __cook(self, _lang, _header, _recipe):
        self.lang = _lang
        self.url = Post.__makeup_url(_lang, _recipe.url)
        self.recipe_id = _recipe.id

        self.title = _header.title
        self.sub_title = _header.sub_title

        self.recipe_yield = _header.recipe_yield
        self.recipe_cuisine = _header.recipe_cuisine
        self.recipe_category = _header.recipe_category

        self.published_at = _recipe.published_at
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
        template = templateEnv.get_template("admin/recipe/render_%s.html" % lang)
        _text = template.render(v={
            "r": recipe,
            "h": head
        })

        self.text = _text

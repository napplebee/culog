# -*- coding: utf-8 -*-

from app.core import db
import datetime as dt


class Post(db.Model):
    __tablename__ = 'ng_posts'

    id = db.Column(db.Integer, primary_key=True, )
    url = db.Column(db.String)
    lang = db.Column(db.String)

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
    def cook_from(recipe):
        posts = Post.query.filter(Post.id == recipe.id).all()

        en_post = None
        def add_en_to_session(_): db.session.merge(_)
        ru_post = None
        def add_ru_to_session(_): db.session.merge(_)

        for p in posts:
            if p.lang == "en":
                en_post = p
            elif p.lang == "ru":
                ru_post = p
            else:
                raise ValueError("Unknown language '%s' of post %s" % (p.lang, p.id))

        if en_post is None:
            en_post = Post()
            def add_en_to_session(_): db.session.add(_)
        if ru_post is None:
            ru_post = Post()
            def add_en_to_session(_): db.session.add(_)

        def __cook(_post, _lang, _header, _recipe):
            _post.lang = _lang
            _post.url = Post.__makeup_url(_lang, _recipe.url)
            _post.recipe_id = _recipe.id

            _post.title = _header.title
            _post.sub_title = _header.sub_title

            _post.recipe_yield = _header.recipe_yield
            _post.recipe_cuisine = _header.recipe_cuisine
            _post.recipe_category = _header.recipe_category

            _post.published_at = _recipe.published_at
            _post.updated_at = dt.datetime.utcnow()

            _post.fb_og_title = _recipe.fb_og_title
            _post.fb_og_description = _recipe.fb_og_description
            _post.fb_og_image = _recipe.fb_og_image
            _post.meta_keywords = _header.meta_keywords
            _post.meta_description = _header.meta_description
            _post.cut = _header.cut
            _post.render(_recipe)
            return _post

        en_post = __cook(en_post, "en", recipe.recipe_header_en, recipe)
        ru_post = __cook(ru_post, "ru", recipe.recipe_header_ru, recipe)

        add_en_to_session(en_post)
        add_ru_to_session(ru_post)

        db.session.commit()

        return en_post.id, ru_post.id

    @staticmethod
    def __makeup_url(lang, url):
        if not url.startswith("/"):
            url = "/%s" % url
        if not url.endswith("/"):
            url = "%s/" % url
        return "%s%s" % (lang, url)

    def render(self, recipe):
        import jinja2
        from configs import basedir
        import os

        head = None
        if self.lang == "en":
            head = recipe.recipe_header_en
        elif self.lang == "ru":
            head = recipe.recipe_header_ru
        else:
            raise ValueError("Unknown language in render for recipe %s" % recipe.id)

        templateLoader = jinja2.FileSystemLoader(
            searchpath=os.path.join(basedir, "templates")
        )
        templateEnv = jinja2.Environment(loader=templateLoader)
        template = templateEnv.get_template("admin/recipe/render.html")
        _text = template.render(v={
            "r": recipe,
            "h": head
        })

        self.text = _text

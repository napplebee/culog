# -*- coding: utf-8 -*-

from app.core import db
import datetime
from app.data.admin.recipe_header_en import RecipeHeaderEn
from app.data.admin.recipe_header_ru import RecipeHeaderRu


class Recipe(db.Model):
    __tablename__ = 'recipe'

    id = db.Column(db.Integer, primary_key=True,)

    name = db.Column(db.String)

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    published_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime)

    visible = db.Column(db.Boolean)

    fb_likes = db.Column(db.Integer)
    fb_og_type = db.Column(db.String)
    fb_og_image = db.Column(db.String)

    cook_time = db.Column(db.String)
    prep_time = db.Column(db.String)

    total_fats = db.Column(db.Numeric)
    total_carbs = db.Column(db.Numeric)
    total_proteins = db.Column(db.Numeric)

    recipe_header_ru = db.relationship("RecipeHeaderRu", uselist=False, backref="recipe", lazy="select")
    recipe_header_en = db.relationship("RecipeHeaderEn", uselist=False, backref="recipe", lazy="select")

    def __init__(self):
        pass

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        pass

    @staticmethod
    def populate_from_ui(form):
        post = Recipe()

        if form.id.data.isdigit():
            post.id = form.id.data

        post.name = form.name.data
        post.url = form.url.data
        post.published_at = form.published_at.data
        post.visible = form.visible.data

        post.cook_time = form.cook_time.data
        post.prep_time = form.prep_time.data
        post.total_fats = form.total_fats.data
        post.total_carbs = form.total_carbs.data
        post.total_proteins = form.total_proteins.data

        post.recipe_header_en = RecipeHeaderEn.populate_from_ui(
            form.recipe_header_en.form)
        post.recipe_header_ru = RecipeHeaderRu.populate_from_ui(
            form.recipe_header_ru.form)

        return post

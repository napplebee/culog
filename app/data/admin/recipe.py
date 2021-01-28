# -*- coding: utf-8 -*-

from app.core import db
import datetime as dt
from app.data.admin.recipe_header_en import RecipeHeaderEn
from app.data.admin.recipe_header_ru import RecipeHeaderRu


class Recipe(db.Model):
    __tablename__ = 'ng_recipe'

    id = db.Column(db.Integer, primary_key=True,)

    name = db.Column(db.String)
    url = db.Column(db.String)

    created_at = db.Column(db.DateTime, default=dt.datetime.utcnow)
    updated_at = db.Column(db.DateTime)

    visible_ru = db.Column(db.Boolean, default=False)
    visible_en = db.Column(db.Boolean, default=False)

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
        return self.id

    def update(self, form):
        if not form.id.data.isdigit():
            raise ValueError("Can't update existing recipe based on form data with no recipe.Id")
        if int(self.id) != int(form.id.data):
            raise ValueError("recipe.id (%s) != form.id (%s)" % (self.id, form.id.data))

        self.name = form.name.data
        self.url = form.url.data

        self.fb_likes = form.fb_likes.data
        self.fb_og_type = form.fb_og_type.data
        self.fb_og_image = form.fb_og_image.data

        self.cook_time = form.cook_time.data
        self.prep_time = form.prep_time.data

        self.total_fats = form.total_fats.data
        self.total_carbs = form.total_carbs.data
        self.total_proteins = form.total_proteins.data

        self.updated_at = dt.datetime.utcnow()

        self.recipe_header_en.merge_with_form(form.recipe_header_en.form)
        self.recipe_header_ru.merge_with_form(form.recipe_header_ru.form)

        db.session.merge(self)
        db.session.commit()

        return self.id

    @staticmethod
    def populate_from_ui(form):
        recipe = Recipe()

        if form.id.data.isdigit():
            recipe.id = form.id.data

        recipe.name = form.name.data
        recipe.url = form.url.data

        recipe.fb_likes = form.fb_likes.data
        recipe.fb_og_type = form.fb_og_type.data
        recipe.fb_og_image = form.fb_og_image.data

        recipe.cook_time = form.cook_time.data
        recipe.prep_time = form.prep_time.data

        recipe.total_fats = form.total_fats.data
        recipe.total_carbs = form.total_carbs.data
        recipe.total_proteins = form.total_proteins.data

        recipe.recipe_header_en = RecipeHeaderEn.populate_from_ui(
            form.recipe_header_en.form)
        recipe.recipe_header_ru = RecipeHeaderRu.populate_from_ui(
            form.recipe_header_ru.form)

        return recipe

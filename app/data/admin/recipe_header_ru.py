# -*- coding: utf-8 -*-

from app.core import db
from app.data.admin.ingredient_type_ru import IngredientTypeRu


class RecipeHeaderRu(db.Model):
    __tablename__ = 'recipe_header_ru'

    id = db.Column(db.Integer, primary_key=True,)

    title = db.Column(db.String)
    sub_title = db.Column(db.String)

    recipe_yield = db.Column(db.String)
    recipe_category = db.Column(db.String)
    recipe_cuisine = db.Column(db.String)

    cut = db.Column(db.Text)
    meta_keywords = db.Column(db.String)
    meta_description = db.Column(db.String)

    fb_og_title = db.Column(db.String)
    fb_og_description = db.Column(db.Text)
    text = db.Column(db.Text)

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    # rename to ingredients_type so it will match
    # the field's name from the form class
    ingredient_types_ru = db.relationship("IngredientTypeRu", backref="recipe_header_ru", lazy="select")

    @staticmethod
    def populate_from_ui(form):
        head = RecipeHeaderRu()

        if form.id.data.isdigit():
            head.id = form.id.data

        head.title = form.title.data
        head.sub_title = form.sub_title.data

        head.recipe_yield = form.recipe_yield.data
        head.recipe_category = form.recipe_category.data
        head.recipe_cuisine = form.recipe_cuisine.data

        head.cut = form.cut.data
        head.meta_keywords = form.meta_keywords.data
        head.meta_description = form.meta_description.data

        head.fb_og_title = form.fb_og_title.data
        head.fb_og_description = form.fb_og_description.data
        head.text = form.text.data

        for ingr_type in form.ingredients_type.entries:
            ingredient_type_ru = IngredientTypeRu.populate_from_form(
                ingr_type.form)
            head.ingredient_types_ru.append(ingredient_type_ru)

        return head
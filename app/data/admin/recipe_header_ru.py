# -*- coding: utf-8 -*-

from app.core import db
from app.data.admin.ingredient_type_ru import IngredientTypeRu


class RecipeHeaderRu(db.Model):
    __tablename__ = 'recipe_header_ru'

    id = db.Column(db.Integer, primary_key=True,)

    title = db.Column(db.String)
    sub_title = db.Column(db.String)

    meta_description = db.Column(db.String)
    meta_keywords = db.Column(db.String)

    cut = db.Column(db.String)
    description = db.Column(db.String)

    image = db.Column(db.String)

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    ingredient_types_ru = db.relationship("IngredientTypeRu", backref="recipe_header_ru", lazy="select")

    @staticmethod
    def populate_from_ui(form):
        head = RecipeHeaderRu()

        if form.id.data.isdigit():
            head.id = form.id.data
        head.sub_title = form.sub_title.data
        head.meta_description = form.meta_description.data
        head.meta_keywords = form.meta_keywords.data
        head.cut = form.cut.data
        head.description = form.descrip.data
        head.image = form.image.data

        for ingr_type in form.ingredients_type.entries:
            ingredient_type_ru = IngredientTypeRu.populate_from_form(
                ingr_type.form)
            head.ingredient_types_ru.append(ingredient_type_ru)

        return head
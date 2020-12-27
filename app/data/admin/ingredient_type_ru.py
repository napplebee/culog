# -*- coding: utf-8 -*-

from app.core import db
from app.data.admin.ingredient_ru import IngredientRu


class IngredientTypeRu(db.Model):
    __tablename__ = 'ingr_type_ru'

    id = db.Column(db.Integer, primary_key=True,)

    name = db.Column(db.String)
    type = db.Column(db.String)
    image = db.Column(db.String)

    recipe_header_ru_id = db.Column(db.Integer, db.ForeignKey('recipe_header_ru.id'), nullable=False)
    ingredients = db.relationship("IngredientRu", backref="ingr_type_ru", lazy="select")

    def merge_with_form(self, form):
        raise ValueError()

    @staticmethod
    def populate_from_form(form):
        ingr_type = IngredientTypeRu()

        if form.id.data.isdigit():
            ingr_type.id = form.id.data
        ingr_type.name = form.name.data
        ingr_type.type = form.name.data
        ingr_type.image = form.name.data

        for ingr in form.ingredients.entries:
            ingr_ru = IngredientRu.populate_from_form(
                ingr.form
            )
            ingr_type.ingredients.append(ingr_ru)

        return ingr_type

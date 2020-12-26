# -*- coding: utf-8 -*-

from app.core import db
from app.data.admin.ingredient_en import IngredientEn


class IngredientTypeEn(db.Model):
    __tablename__ = 'ingr_type_en'

    id = db.Column(db.Integer, primary_key=True,)

    name = db.Column(db.String)
    type = db.Column(db.String)
    image = db.Column(db.String)

    recipe_header_en_id = db.Column(db.Integer, db.ForeignKey('recipe_header_en.id'), nullable=False)
    ingredients = db.relationship("IngredientEn", backref="ingr_type_en", lazy="select")

    @staticmethod
    def populate_from_form(form):
        ingr_type = IngredientTypeEn()

        if form.id.data.isdigit():
            ingr_type.id = form.id.data
        ingr_type.name = form.name.data
        ingr_type.type = form.type.data
        ingr_type.image = form.image.data

        for ingr in form.ingredients.entries:
            ingr_en = IngredientEn.populate_from_form(
                ingr.form
            )
            ingr_type.ingredients.append(ingr_en)

        return ingr_type

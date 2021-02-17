# -*- coding: utf-8 -*-

from app.core import db
from app.data.admin.ingredient_ru import IngredientRu


class IngredientTypeRu(db.Model):
    __tablename__ = 'ng_ingr_type_ru'

    id = db.Column(db.Integer, primary_key=True,)

    name = db.Column(db.String)
    type = db.Column(db.String)
    image = db.Column(db.String)

    recipe_header_ru_id = db.Column(db.Integer, db.ForeignKey('ng_recipe_header_ru.id'), nullable=False)
    ingredients = db.relationship("IngredientRu", backref="ingr_type_ru", lazy="select")

    def delete(self):
        for ing in self.ingredients:
            db.session.delete(ing)

        db.session.delete(self)

    def merge_with_form(self, form):
        if not form.id.data.isdigit():
            raise ValueError("Can't update existing ingredient type based on form data with no ingredient_type.Id")
        if int(self.id) != int(form.id.data):
            raise ValueError("ingredient_type.Id (%s) != form.id (%s)" % (self.id, form.id.data))

        self.name = form.name.data
        self.type = form.type.data
        self.image = form.image.data

        id2ingrs = {}
        new_ingrs = []
        for ingr in form.ingredients.entries:
            if ingr.form.id.data.isdigit():
                id2ingrs[int(ingr.form.id.data)] = ingr.form
            else:
                new_ingrs.append(ingr.form)

        for ingr in self.ingredients:
            if ingr.id in id2ingrs:
                ingr_form = id2ingrs[ingr.id]
                ingr.merge_with_form(ingr_form)
            else:
                db.session.delete(ingr)

        for ing_form in new_ingrs:
            ingr_ru = IngredientRu.populate_from_form(
                ing_form
            )
            self.ingredients.append(ingr_ru)

        return self

    @staticmethod
    def populate_from_form(form):
        ingr_type = IngredientTypeRu()

        if form.id.data.isdigit():
            ingr_type.id = form.id.data
        ingr_type.name = form.name.data
        ingr_type.type = form.type.data
        ingr_type.image = form.image.data

        for ingr in form.ingredients.entries:
            ingr_ru = IngredientRu.populate_from_form(
                ingr.form
            )
            ingr_type.ingredients.append(ingr_ru)

        return ingr_type

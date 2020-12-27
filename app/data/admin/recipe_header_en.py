# -*- coding: utf-8 -*-

import datetime as dt
from app.core import db
from app.data.admin.ingredient_type_en import IngredientTypeEn


class RecipeHeaderEn(db.Model):
    __tablename__ = 'recipe_header_en'

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
    ingredients_type = db.relationship("IngredientTypeEn", backref="recipe_header_en", lazy="select")

    def merge_with_form(self, form):
        if not form.id.data.isdigit():
            raise ValueError("Can't update existing recipe header based on form data with no recipe.Id")
        if int(self.id) != int(form.id.data):
            raise ValueError("recipe_header.id (%s) != form.id (%s)" % (self.id, form.id.data))

        self.title = form.title.data
        self.sub_title = form.sub_title.data

        self.recipe_yield = form.recipe_yield.data
        self.recipe_category = form.recipe_category.data
        self.recipe_cuisine = form.recipe_cuisine.data

        self.cut = form.cut.data
        self.meta_keywords = form.meta_keywords.data
        self.meta_description = form.meta_description.data

        self.fb_og_title = form.fb_og_title.data
        self.fb_og_description = form.fb_og_description.data
        self.text = form.text.data

        id2ing_types = {}
        new_ing_types = []
        for it in form.ingredients_type.entries:
            if it.form.id.data.isdigit():
                id2ing_types[int(it.form.id.data)] = it.form
            else:
                new_ing_types.append(it.form)

        to_be_removed = []
        for ingrType in self.ingredients_type:
            if ingrType.id in id2ing_types:
                # then updating
                ingr_type_form = id2ing_types[ingrType.id]
                ingrType.merge_with_form(ingr_type_form)
            else:
                db.session.delete(ingrType)
                # to_be_removed.append(ingrType)

        for _ in to_be_removed:
            self.ingredients_type.remove(_)

        for ing_type_form in new_ing_types:
            ingredient_type_en = IngredientTypeEn.populate_from_form(ing_type_form)
            self.ingredients_type.append(ingredient_type_en)

        return self

    @staticmethod
    def populate_from_ui(form):
        head = RecipeHeaderEn()

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
            ingredient_type_en = IngredientTypeEn.populate_from_form(
                ingr_type.form)
            head.ingredients_type.append(ingredient_type_en)

        return head


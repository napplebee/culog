# -*- coding: utf-8 -*-

from app.core import db
from app.data.admin.ingredient_type_en import IngredientTypeEn
from app.data.admin.process_type_en import ProcessTypeEn


class RecipeHeaderEn(db.Model):
    __tablename__ = 'ng_recipe_header_en'

    id = db.Column(db.Integer, primary_key=True,)

    title = db.Column(db.String)
    sub_title = db.Column(db.String)

    recipe_yield = db.Column(db.String)
    recipe_yield_number = db.Column(db.Integer)
    recipe_category = db.Column(db.String)
    recipe_cuisine = db.Column(db.String)

    meta_keywords = db.Column(db.String)
    meta_description = db.Column(db.String)

    fb_og_title = db.Column(db.String)
    fb_og_description = db.Column(db.Text)

    cut = db.Column(db.Text)
    text = db.Column(db.Text)

    recipe_id = db.Column(db.Integer, db.ForeignKey('ng_recipe.id'), nullable=False)
    ingredients_type = db.relationship("IngredientTypeEn", backref="recipe_header_en", lazy="select",
                                       order_by="IngredientTypeEn.pos")
    process_type = db.relationship("ProcessTypeEn", backref="process_type_en", lazy="select",
                                   order_by="ProcessTypeEn.pos")

    def merge_with_form(self, form):
        if not form.id.data.isdigit():
            raise ValueError("Can't update existing recipe header based on form data with no recipe.Id")
        if int(self.id) != int(form.id.data):
            raise ValueError("recipe_header.id (%s) != form.id (%s)" % (self.id, form.id.data))

        self.title = form.title.data
        self.sub_title = form.sub_title.data

        self.recipe_yield = form.recipe_yield.data
        self.recipe_yield_number = form.recipe_yield_number.data
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
        for st in form.ingredients_type.entries:
            if st.form.id.data.isdigit():
                id2ing_types[int(st.form.id.data)] = st.form
            elif not st.form.empty():
                new_ing_types.append(st.form)

        for ingrType in self.ingredients_type:
            if ingrType.id in id2ing_types:
                # then updating
                ingr_type_form = id2ing_types[ingrType.id]
                ingrType.merge_with_form(ingr_type_form)
            else:
                ingrType.delete()

        for ing_type_form in new_ing_types:
            ingredient_type_en = IngredientTypeEn.populate_from_form(ing_type_form)
            self.ingredients_type.append(ingredient_type_en)

        id2process_types = {}
        new_process_types = []
        for st in form.process_type.entries:
            if st.form.id.data.isdigit():
                id2process_types[int(st.form.id.data)] = st.form
            elif not st.form.empty():
                new_process_types.append(st.form)

        for processType in self.process_type:
            if processType.id in id2process_types:
                # then updating
                proc_type_form = id2process_types[processType.id]
                processType.merge_with_form(proc_type_form)
            else:
                processType.delete()

        for proc_type_form in new_process_types:
            proc_type_en = ProcessTypeEn.populate_from_form(proc_type_form)
            self.process_type.append(proc_type_en)

        return self

    @staticmethod
    def populate_from_ui(form):
        head = RecipeHeaderEn()

        if form.id.data.isdigit():
            head.id = form.id.data

        head.title = form.title.data
        head.sub_title = form.sub_title.data

        head.recipe_yield = form.recipe_yield.data
        head.recipe_yield_number = form.recipe_yield_number.data
        head.recipe_category = form.recipe_category.data
        head.recipe_cuisine = form.recipe_cuisine.data

        head.cut = form.cut.data
        head.meta_keywords = form.meta_keywords.data
        head.meta_description = form.meta_description.data

        head.fb_og_title = form.fb_og_title.data
        head.fb_og_description = form.fb_og_description.data
        head.text = form.text.data

        for ingr_type in form.ingredients_type.entries:
            ingredient_type_en = IngredientTypeEn.populate_from_form(ingr_type.form)
            head.ingredients_type.append(ingredient_type_en)

        for proc_type in form.process_type.entries:
            process_type_en = ProcessTypeEn.populate_from_form(proc_type.form)
            head.process_type.append(process_type_en)

        # process_type

        return head


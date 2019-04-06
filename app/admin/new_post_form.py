# -*- coding: utf-8 -*-

# http://wtforms.simplecodes.com/docs/1.0.1/fields.html#field-enclosures
# http://wtforms.simplecodes.com/docs/1.0.1/fields.html#wtforms.fields.FieldList

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField, BooleanField, TextAreaField, HiddenField, DateField, FieldList, FormField


class IngredientForm(Form):
    name = StringField("Ingredient name:")
    amount_value = StringField("Amount:")
    amount_type = StringField("Amount type:")

    note = TextAreaField("Note:")

    optional = BooleanField("Optional?")


class IngredientTypeForm(Form):
    name = StringField("Name:")
    note = TextAreaField("Note:")
    image = StringField("Image:")

    ingredients = FieldList(FormField(IngredientForm))


class PostForm(Form): # post + post_header
    title = StringField()
    sub_title = StringField()
    cut = StringField()
    meta_description = StringField()
    meta_keywords = StringField()
    description = StringField()
    image = StringField()
    recipe_category = StringField()
    recipe_cuisine = StringField()
    recipe_yield = StringField()
    total_fats = StringField()
    total_carbs = StringField()
    total_proteins = StringField()

    prep_time = StringField()
    cook_time = StringField()

    published_at = DateField("Published:")
    visible = BooleanField("Visible?")







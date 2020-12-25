from flask.ext.wtf import Form
from wtforms import StringField, SubmitField,\
    SelectField, BooleanField, TextAreaField,\
    HiddenField, DateField, FieldList, FormField, FloatField

from app.common.facebook import OG_TYPES
from configs import Config as cfg


class IngredientForm(Form):
    id = HiddenField()
    name = StringField("Ingredient&nbsp;name:")
    amount = StringField("Amount:")
    amount_type = SelectField("Amount&nbsp;type:", choices=[
        (_, _) for _ in cfg.AMOUNT_TYPES
    ])

    note = StringField("Note:")
    is_optional = BooleanField("Optional?")


class IngredientTypeForm(Form):
    id = HiddenField()
    name = StringField("Name:")
    type = StringField("Type:")
    image = StringField("Image:")

    ingredients = FieldList(FormField(IngredientForm), "Ingredients", min_entries=1)


class RecipeHeaderForm(Form):
    id = HiddenField()
    title = StringField("Title:")
    sub_title = StringField("Subtitle:")

    recipe_yield = StringField("Number of servings:")
    recipe_category = StringField("Recipe category")
    recipe_cuisine = StringField("Recipe cuisine")

    cut = TextAreaField("Cut:")
    meta_keywords = StringField("Keywords (meta):")
    meta_description = StringField("Description (meta):")

    fb_og_title = StringField("FB og_title:")
    fb_og_description = TextAreaField("FB og_description:")
    text = TextAreaField("Text:")

    ingredients_type = FieldList(FormField(IngredientTypeForm), "Ingredient types:", min_entries=1)


class RecipeForm(Form):
    id = HiddenField()

    name = StringField("Name")
    url = StringField("URL:")
    published_at = DateField("Published:")

    visible = BooleanField("Visible?")

    fb_likes = StringField("FB likes:")
    og_type = SelectField("FB og_type:", choices=[(t, t) for t in OG_TYPES])
    og_image = StringField("FB og_image")

    cook_time = StringField("Cook time:")
    prep_time = StringField("Preparation time:")

    total_fats = FloatField("Fats:")
    total_carbs = FloatField("Carbs:")
    total_proteins = FloatField("Proteins:")

    recipe_header_ru = FormField(RecipeHeaderForm, "BlogPostHeader (ru)")
    recipe_header_en = FormField(RecipeHeaderForm, "BlogPostHeader (en)")

    submit = SubmitField("Save")

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField,\
    SelectField, BooleanField, TextAreaField,\
    HiddenField, DateField, FieldList, FormField, FloatField

from app.common.facebook import OG_TYPES


class IngredientForm(Form):
    id = HiddenField()
    name = StringField("Ingredient&nbsp;name:")
    amount = StringField("Amount:")
    amount_type = StringField("Amount&nbsp;type:")

    note = StringField("Note:")
    is_optional = BooleanField("Optional?")


class IngredientTypeForm(Form):
    id = HiddenField()
    name = StringField("Name:")
    note = StringField("Note:")
    image = StringField("Image:")

    ingredients = FieldList(FormField(IngredientForm), "Ingredients", min_entries=1)


class BlogPostHeaderForm(Form):
    id = HiddenField()
    title = StringField("Title:")
    sub_title = StringField("Subtitle:")

    meta_description = StringField("Description (meta):")
    meta_keywords = StringField("Keywords (meta):")

    cut = TextAreaField("Cut:")
    descrip = TextAreaField("Description:")

    image = StringField("Image")

    ingredients_type = FieldList(FormField(IngredientTypeForm), "Ingredient types:", min_entries=1)


class BlogPostForm(Form):
    id = HiddenField()

    name = StringField("Name")
    url = StringField("URL:")
    published_at = DateField("Published:")

    visible = BooleanField("Visible?")

    # fb_likes = db.Column(db.Integer)
    # og_type = db.Column(db.String)
    # og_image = db.Column(db.String)

    cook_time = StringField("Cook time:")
    prep_time = StringField("Preparation time:")

    total_fats = FloatField("Fats:")
    total_carbs = FloatField("Carbs:")
    total_proteins = FloatField("Proteins:")

    blog_post_header_ru = FormField(BlogPostHeaderForm, "BlogPostHeader (ru)")
    blog_post_header_en = FormField(BlogPostHeaderForm, "BlogPostHeader (en)")

    submit = SubmitField("Save")

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField,\
    SelectField, BooleanField, TextAreaField,\
    HiddenField, DateField, FieldList, FormField, FloatField

from app.common.facebook import OG_TYPES
from app.common.constants import Constants as cnst


class PostForm(Form):
    # common fields
    id = HiddenField()
    url = StringField("URL:")
    lang = StringField("Language:")
    visible = BooleanField("Visible?")

    title = StringField("Title:")
    sub_title = StringField("Sub title:")

    recipe_yield = StringField("Recipe yield:")
    recipe_cuisine = StringField("Recipe cuisine:")
    recipe_category = StringField("Recipe category:")

    published_at = DateField("Published:")

    fb_likes = StringField("Fb likes:")
    fb_og_image = StringField("FB og_image:")
    fb_og_title = StringField("FB og_title:")
    fb_og_description = StringField("FB og_description:")

    meta_keywords = StringField("Meta keywords:")
    meta_description = TextAreaField("Meta description:")

    cook_time = StringField("Cook time:")
    prep_time = StringField("Prep time:")

    total_fats = StringField("Fats:")
    total_carbs = StringField("Carbs:")
    total_proteins = StringField("Proteins:")

    cut = TextAreaField("Cut:")
    text = TextAreaField("Text:")

    submit = SubmitField()


class ProcessStepForm(Form):
    id = HiddenField()
    description = StringField("Description:")
    note = TextAreaField("Note:")
    image = StringField("Image:")

    def empty(self):
        return self.id.data == "" and self.description.data == "" and self.note.data == "" and self.image.data == ""


class ProcessTypeForm(Form):
    id = HiddenField()
    name = StringField("Name:")
    note = TextAreaField("Note:")

    steps = FieldList(FormField(ProcessStepForm), "Steps", min_entries=1)

    def empty(self):
        return self.id.data == "" and self.name.data == "" and self.note.data == ""


class IngredientForm(Form):
    id = HiddenField()
    name = StringField("Ingredient&nbsp;name:")
    amount_value = StringField("Amount:")
    amount_type = SelectField("Amount&nbsp;type:", choices=[
        (_, _) for _ in cnst.AMOUNT_TYPES
    ])

    note = StringField("Note:")
    optional = BooleanField("Optional?")

    def empty(self):
        return self.id.data == "" and self.name.data == "" and self.amount_value.data == "" and self.note.data == ""


class IngredientTypeForm(Form):
    id = HiddenField()
    name = StringField("Name:")
    type = StringField("Type:")
    image = StringField("Image:")

    ingredients = FieldList(FormField(IngredientForm), "Ingredients", min_entries=1)

    def empty(self):
        return self.id.data == "" and self.name.data == "" and self.type.data == "" and self.image.data == ""


class RecipeHeaderForm(Form):
    id = HiddenField()
    title = StringField("Title:")
    sub_title = StringField("Subtitle:")

    recipe_yield = StringField("Number of servings:")
    recipe_category = StringField("Recipe category")
    recipe_cuisine = StringField("Recipe cuisine")

    cut = TextAreaField("Cut:")
    meta_keywords = StringField("Keywords (meta):")
    meta_description = TextAreaField("Description (meta):")

    fb_og_title = StringField("FB og_title:")
    fb_og_description = TextAreaField("FB og_description:")
    text = TextAreaField("Text:")

    ingredients_type = FieldList(FormField(IngredientTypeForm), "Ingredient types:", min_entries=1)
    process_type = FieldList(FormField(ProcessTypeForm), "Process types:", min_entries=1)


class RecipeForm(Form):
    id = HiddenField()

    name = StringField("Name")
    url = StringField("URL:")
    published_at = DateField("Published:")

    fb_likes = StringField("FB likes:")
    fb_og_type = SelectField("FB og_type:", choices=[(t, t) for t in OG_TYPES])
    fb_og_image = StringField("FB og_image")

    cook_time = StringField("Cook time:")
    prep_time = StringField("Preparation time:")

    total_fats = FloatField("Fats:")
    total_carbs = FloatField("Carbs:")
    total_proteins = FloatField("Proteins:")

    recipe_header_ru = FormField(RecipeHeaderForm, "BlogPostHeader (ru)")
    recipe_header_en = FormField(RecipeHeaderForm, "BlogPostHeader (en)")

    submit = SubmitField("Save")

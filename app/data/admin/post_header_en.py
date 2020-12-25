# -*- coding: utf-8 -*-

from app.core import db
from app.data.admin.ingredient_type_en import IngredientTypeEn


class PostHeaderEn(db.Model):
    __tablename__ = 'post_header_en'

    id = db.Column(db.Integer, primary_key=True,)

    title = db.Column(db.String)
    sub_title = db.Column(db.String)

    meta_description = db.Column(db.String)
    meta_keywords = db.Column(db.String)

    cut = db.Column(db.String)
    description = db.Column(db.String)

    image = db.Column(db.String)

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    ingredient_types_en = db.relationship("IngredientTypeEn", backref="post_header_en", lazy="select")

    @staticmethod
    def populate_from_ui(form):
        head = PostHeaderEn()

        if form.id.data.isdigit():
            head.id = form.id.data
        head.sub_title = form.sub_title.data
        head.meta_description = form.meta_description.data
        head.meta_keywords = form.meta_keywords.data
        head.cut = form.cut.data
        head.description = form.descrip.data
        head.image = form.image.data

        for ingr_type in form.ingredients_type.entries:
            ingredient_type_en = IngredientTypeEn.populate_from_form(
                ingr_type.form)
            head.ingredient_types_en.append(ingredient_type_en)

        return head


# -*- coding: utf-8 -*-

from app.core import db
import datetime


class IngredientTypeRu(db.Model):
    __tablename__ = 'ingr_type_ru'

    id = db.Column(db.Integer, primary_key=True,)

    name = db.Column(db.String)
    type = db.Column(db.String)
    image = db.Column(db.String)

    post_header_ru_id = db.Column(db.Integer, db.ForeignKey('post_header_ru.id'), nullable=False)
    ingredients_ru = db.relationship("ingr_ru", backref="ingr_type_ru", lazy="select")

# -*- coding: utf-8 -*-

from app.core import db
import datetime


class IngredientTypeRu(db.Model):
    __tablename__ = 'ingr_type_ru'

    id = db.Column(db.Integer, primary_key=True,)

    name = db.Column(db.String)
    type = db.Column(db.String)
    image = db.Column(db.String)

    # created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    # published_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    # updated_at = db.Column(db.DateTime)

    # visible = db.Column(db.Boolean)

    # url = db.Column(db.String, unique=True)
    # fb_likes = db.Column(db.Integer)
    # og_type = db.Column(db.String)
    # og_image = db.Column(db.String)

    # cook_time = db.Column(db.String)
    # prep_time = db.Column(db.String)

    # todo: tweak lazy value depends on use cases
    # translations = db.relationship("Translation", backref="post", lazy="select")

    post_header_ru_id = db.Column(db.Integer, db.ForeignKey('post_header_ru.id'), nullable=False)

    ingredients_ru = db.relationship("ingr_ru", backref="ingr_type_ru", lazy="select")

# -*- coding: utf-8 -*-

from app.core import db
import datetime


class PostHeaderRu(db.Model):
    __tablename__ = 'post_header_ru'

    id = db.Column(db.Integer, primary_key=True,)

    title = db.Column(db.String)
    sub_title = db.Column(db.String)

    meta_description = db.Column(db.String)
    meta_keywords = db.Column(db.String)

    cut = db.Column(db.String)
    description = db.Column(db.String)

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
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    ingredient_types_ru = db.relationship("ingr_type_ru", backref="post_header_ru", lazy="select")
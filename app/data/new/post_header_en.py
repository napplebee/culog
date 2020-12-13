# -*- coding: utf-8 -*-

from app.core import db
import datetime


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
    ingredient_types_en = db.relationship("ingr_type_en", backref="post_header_en", lazy="select")

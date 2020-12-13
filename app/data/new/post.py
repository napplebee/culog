# -*- coding: utf-8 -*-

from app.core import db
import datetime


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True,)

    name = db.Column(db.String)

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    published_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime)

    visible = db.Column(db.Boolean)

    # url = db.Column(db.String, unique=True)
    # fb_likes = db.Column(db.Integer)
    # og_type = db.Column(db.String)
    # og_image = db.Column(db.String)

    cook_time = db.Column(db.String)
    prep_time = db.Column(db.String)

    total_fats = db.Column(db.Numeric)
    total_carbs = db.Column(db.Numeric)
    total_proteins = db.Column(db.Numeric)

    post_header_ru = db.relationship("post_header_ru", backref="post", lazy="select")
    post_header_en = db.relationship("post_header_en", backref="post", lazy="select")

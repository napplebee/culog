# -*- coding: utf-8 -*-

from app.core import db
import datetime


class Post(db.Model):
    __tablename__ = 'ng_posts'

    id = db.Column(db.Integer, primary_key=True, )
    url = db.Column(db.String)
    lang = db.Column(db.String)

    title = db.Column(db.String)
    sub_title = db.Column(db.String)
    recipe_category = db.Column(db.String)

    published_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    fb_og_image = db.Column(db.String)

    cut = db.Column(db.Text)
    meta_keywords = db.Column(db.String)
    meta_description = db.Column(db.String)

    text = db.Column(db.Text)


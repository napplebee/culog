# -*- coding: utf-8 -*-

from app.core import db
import datetime


class Post(db.Model):
    __tablename__ = 'ng_posts'

    id = db.Column(db.Integer, primary_key=True, )
    url = db.Column(db.String)
    lang = db.Column(db.String)

    published_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    fb_likes = db.Column(db.Integer)
    fb_og_type = db.Column(db.String)
    fb_og_image = db.Column(db.String)

    cook_time = db.Column(db.String)
    prep_time = db.Column(db.String)

    total_fats = db.Column(db.Numeric)
    total_carbs = db.Column(db.Numeric)
    total_proteins = db.Column(db.Numeric)

    title = db.Column(db.String)
    sub_title = db.Column(db.String)
    image = db.Column(db.String)

    recipe_yield = db.Column(db.String)
    recipe_category = db.Column(db.String)
    recipe_cuisine = db.Column(db.String)

    cut = db.Column(db.Text)
    meta_keywords = db.Column(db.String)
    meta_description = db.Column(db.String)

    fb_og_title = db.Column(db.String)
    fb_og_description = db.Column(db.Text)
    text = db.Column(db.Text)


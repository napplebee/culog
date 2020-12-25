# -*- coding: utf-8 -*-

from app.core import db
import datetime
from app.data.admin.post_header_en import PostHeaderEn
from app.data.admin.post_header_ru import PostHeaderRu


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

    post_header_ru = db.relationship("PostHeaderRu", uselist=False, backref="post", lazy="select")
    post_header_en = db.relationship("PostHeaderEn", uselist=False, backref="post", lazy="select")

    def __init__(self):
        pass

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        pass

    @staticmethod
    def populate_from_ui(post_form):
        post = Post()

        if post_form.id.data.isdigit():
            post.id = post_form.id.data

        post.name = post_form.name.data
        post.url = post_form.url.data
        post.published_at = post_form.published_at.data
        post.visible = post_form.visible.data

        post.cook_time = post_form.cook_time.data
        post.prep_time = post_form.prep_time.data
        post.total_fats = post_form.total_fats.data
        post.total_carbs = post_form.total_carbs.data
        post.total_proteins = post_form.total_proteins.data

        post.post_header_en = PostHeaderEn.populate_from_ui(
            post_form.blog_post_header_en.form)
        post.post_header_ru = PostHeaderRu.populate_from_ui(
            post_form.blog_post_header_ru.form)

        return post

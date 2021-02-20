# -*- coding: utf-8 -*-

from app.core import db
import datetime
from app.common.constants import Constants as cnst


class Translation(db.Model):
    __tablename__ = "translation"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    value = db.Column(db.Text)
    lang = db.Column(db.Enum(*cnst.SUPPORTED_LANGS, name="langs", native_enum=False))

    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime)
    generated_at = db.Column(db.DateTime)

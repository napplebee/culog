# -*- coding: utf-8 -*-

from app.core import db
import datetime
from configs import Config as cfg


class IngredientRu(db.Model):
    __tablename__ = 'ingr_ru'

    id = db.Column(db.Integer, primary_key=True,)

    name = db.Column(db.String)
    amount_value = db.Column(db.Float)
    amount_type = db.Column(db.Enum(*cfg.AMOUNT_TYPES, name="amount_type", native_enum=False)) # enum

    note = db.Column(db.String)
    optional = db.Column(db.Boolean) # boolean

    # todo: tweak lazy value depends on use cases
    # translations = db.relationship("Translation", backref="post", lazy="select")

    ingr_type_id = db.Column(db.Integer, db.ForeignKey('ingr_type_ru.id'), nullable=False)


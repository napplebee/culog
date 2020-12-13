# -*- coding: utf-8 -*-

from app.core import db
import datetime
from configs import Config as cfg


class IngredientEn(db.Model):
    __tablename__ = 'ingr_en'

    id = db.Column(db.Integer, primary_key=True,)

    name = db.Column(db.String)
    amount_value = db.Column(db.Float)
    # enum
    amount_type = db.Column(db.Enum(*cfg.AMOUNT_TYPES, name="amount_type", native_enum=False))

    note = db.Column(db.String)
    optional = db.Column(db.Boolean) # boolean

    ingr_type_id = db.Column(db.Integer, db.ForeignKey('ingr_type_en.id'), nullable=False)


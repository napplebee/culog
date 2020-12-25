# -*- coding: utf-8 -*-

from app.core import db
from configs import Config as cfg


class IngredientRu(db.Model):
    __tablename__ = 'ingr_ru'

    id = db.Column(db.Integer, primary_key=True,)

    name = db.Column(db.String)
    amount_value = db.Column(db.String)
    # enum
    amount_type = db.Column(db.Enum(*cfg.AMOUNT_TYPES, name="amount_type", native_enum=False))

    note = db.Column(db.String)
    optional = db.Column(db.Boolean) # boolean

    ingr_type_id = db.Column(db.Integer, db.ForeignKey('ingr_type_ru.id'), nullable=False)

    @staticmethod
    def populate_from_form(form):
        ingr = IngredientRu()

        if form.id.data.isdigit():
            ingr.id = form.id.data
        ingr.name = form.name.data
        ingr.amount_value = form.amount.data
        ingr.amount_type = form.amount_type.data
        ingr.note = form.note.data
        ingr.optional = form.is_optional.data

        return ingr



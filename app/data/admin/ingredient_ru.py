# -*- coding: utf-8 -*-

from app.core import db
from configs import Config as cfg


class IngredientRu(db.Model):
    __tablename__ = 'ng_ingr_ru'

    id = db.Column(db.Integer, primary_key=True,)

    name = db.Column(db.String)
    amount_value = db.Column(db.String)
    # enum
    amount_type = db.Column(db.Enum(*cfg.AMOUNT_TYPES, name="amount_type", native_enum=False))

    note = db.Column(db.String)
    optional = db.Column(db.Boolean) # boolean

    ingr_type_id = db.Column(db.Integer, db.ForeignKey('ng_ingr_type_ru.id'), nullable=False)

    def merge_with_form(self, form):
        if not form.id.data.isdigit():
            raise ValueError("Can't update existing ingredient based on form data with no ingredient.Id")
        if int(self.id) != int(form.id.data):
            raise ValueError("ingredient.Id (%s) != form.id (%s)" % (self.id, form.id.data))

        self.name = form.name.data
        self.amount_value = form.amount_value.data
        self.amount_type = form.amount_type.data
        self.note = form.note.data
        self.optional = form.optional.data

        return self

    @staticmethod
    def populate_from_form(form):
        ingr = IngredientRu()

        if form.id.data.isdigit():
            ingr.id = form.id.data
        ingr.name = form.name.data
        ingr.amount_value = form.amount_value.data
        ingr.amount_type = form.amount_type.data
        ingr.note = form.note.data
        ingr.optional = form.optional.data

        return ingr



# -*- coding: utf-8 -*-

import datetime as dt
from app.common.utils import zero_if_none
from app.core import db


class ProcessStepRu(db.Model):
    __tablename__ = 'ng_process_step_ru'

    id = db.Column(db.Integer, primary_key=True, )

    description = db.Column(db.String)
    image = db.Column(db.String)
    note = db.Column(db.String)
    pos = db.Column(db.Integer)

    process_type_id = db.Column(db.Integer, db.ForeignKey('ng_process_type_ru.id'), nullable=False)

    def get_image_src(self):
        return self.image.split("|")[0].strip()

    def get_small_image_src(self):
        image_path = self.image.split("|")[0].strip()
        image_path_length = len(image_path)
        return image_path[:image_path_length - 4] + "_small.jpg"

    def get_image_alt(self, default):
        try:
            return self.image.split("|")[1].strip()
        except IndexError:
            return default

    def merge_with_form(self, form):
        if not form.id.data.isdigit():
            raise ValueError("Can't update existing process step based on form data with no processStep .Id")
        if int(self.id) != int(form.id.data):
            raise ValueError("processStep.Id (%s) != form.id (%s)" % (self.id, form.id.data))

        self.description = form.description.data
        self.image = form.image.data
        self.note = form.note.data
        self.pos = int(zero_if_none(form.pos.data))

        return self

    @staticmethod
    def populate_from_form(form):
        st = ProcessStepRu()

        if form.id.data.isdigit():
            st.id = form.id.data

        st.description = form.description.data
        st.image = form.image.data
        st.note = form.note.data
        st.pos = int(zero_if_none(form.pos.data))

        return st

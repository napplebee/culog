# -*- coding: utf-8 -*-

import datetime as dt
from app.core import db


class ProcessStepEn(db.Model):
    __tablename__ = 'ng_process_step_en'

    id = db.Column(db.Integer, primary_key=True, )

    description = db.Column(db.String)
    image = db.Column(db.String)
    note = db.Column(db.String)

    process_type_id = db.Column(db.Integer, db.ForeignKey('ng_process_type_en.id'), nullable=False)

    def merge_with_form(self, form):
        if not form.id.data.isdigit():
            raise ValueError("Can't update existing process step based on form data with no processStep .Id")
        if int(self.id) != int(form.id.data):
            raise ValueError("processStep.Id (%s) != form.id (%s)" % (self.id, form.id.data))

        self.description = form.description.data
        self.image = form.image.data
        self.note = form.note.data

        return self

    @staticmethod
    def populate_from_form(form):
        st = ProcessStepEn()

        if form.id.data.isdigit():
            st.id = form.id.data

        st.description = form.description.data
        st.image = form.image.data
        st.note = form.note.data

        return st

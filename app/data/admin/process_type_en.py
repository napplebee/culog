# -*- coding: utf-8 -*-

import datetime as dt
from app.core import db
from app.data.admin.process_step_en import ProcessStepEn


class ProcessTypeEn(db.Model):
    __tablename__ = 'ng_process_type_en'

    id = db.Column(db.Integer, primary_key=True, )

    name = db.Column(db.String)
    note = db.Column(db.String)

    recipe_header_en_id = db.Column(db.Integer, db.ForeignKey('ng_recipe_header_en.id'), nullable=False)
    steps = db.relationship("ProcessStepEn", backref="process_type_en", lazy="select")

    def merge_with_form(self, form):
        if not form.id.data.isdigit():
            raise ValueError("Can't update existing process type based on form data with no process_type.Id")
        if int(self.id) != int(form.id.data):
            raise ValueError("process_type.Id (%s) != form.id (%s)" % (self.id, form.id.data))

        self.name = form.name.data
        self.note = form.note.data

        id2steps = {}
        new_steps = []
        for step in form.steps.entries:
            if step.form.id.data.isdigit():
                id2steps[int(step.form.id.data)] = step.form
            else:
                new_steps.append(step.form)

        for step in self.steps:
            if step.id in id2steps:
                step_form = id2steps[step.id]
                step.merge_with_form(step_form)
            else:
                db.session.delete(step)

        for step_form in new_steps:
            step_en = ProcessStepEn.populate_from_form(
                step_form
            )
            self.steps.append(step_en)

        return self

    @staticmethod
    def populate_from_form(form):
        proc_type = ProcessTypeEn()

        if form.id.data.isdigit():
            proc_type.id = form.id.data

        proc_type.name = form.name.data
        proc_type.note = form.note.data

        for st in form.steps.entries:
            step = ProcessStepEn.populate_from_form(st.form)
            proc_type.steps.append(step)

        return proc_type

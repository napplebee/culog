from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField, BooleanField, TextAreaField, HiddenField, DateField

from app.common.facebook import OG_TYPES


class BlogPostForm(Form):
    pass
# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField, BooleanField, TextAreaField, HiddenField, DateField

from app.common.facebook import OG_TYPES


class BlogPostForm(Form):
    # common fields
    id = HiddenField()
    name = StringField("Name (for internal purpose):")
    url = StringField("URL:")
    published_at = DateField("Published:")

    visible = BooleanField("Visible?")
    is_article = BooleanField("Is article?")
    og_type = SelectField("FB og_type:", choices=[(t, t) for t in OG_TYPES])
    og_image = StringField("FB og_image:")
    # todo: fb_likes -- show as info with disabled field ??

    cook_time = StringField("Cooking time:")
    prep_time = StringField("Preparation time:")

    # english specific fields
    en_title = StringField("Title:")
    en_sub_title = StringField("Subtitle:")
    en_keywords = StringField("Keywords (meta):")
    en_description = TextAreaField("Description (meta):")
    en_og_title = StringField("FB og_title:")
    en_og_description = TextAreaField("FB og_description:")
    en_blog_cut = TextAreaField("Cut:")
    en_blog_text = TextAreaField("Text:")

    # russian specific fields
    ru_title = StringField(u"Title:")
    ru_sub_title = StringField(u"Subtitle:")
    ru_keywords = StringField(u"Keywords (meta):")
    ru_description = TextAreaField(u"Description (meta):")
    ru_og_title = StringField(u"FB og_title:")
    ru_og_description = TextAreaField(u"FB og_description:")
    ru_blog_cut = TextAreaField(u"Cut:")
    ru_blog_text = TextAreaField(u"Text:")

    # swedish specific fields
    sv_title = StringField(u"Title:")
    sv_sub_title = StringField(u"Subtitle:")
    sv_keywords = StringField(u"Keywords (meta):")
    sv_description = TextAreaField(u"Description (meta):")
    sv_og_title = StringField(u"FB og_title:")
    sv_og_description = TextAreaField(u"FB og_description:")
    sv_blog_cut = TextAreaField(u"Cut:")
    sv_blog_text = TextAreaField(u"Text:")

    # util fields
    submit = SubmitField()

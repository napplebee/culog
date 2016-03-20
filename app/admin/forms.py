# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField, BooleanField, TextAreaField
from wtforms.validators import Required

from app.common.facebook import OG_TYPES


class BlogPostForm(Form):
    # common fields
    name = StringField("Name (for internal purpose):")
    url = StringField("URL:")

    visible = BooleanField("Visible?")
    og_type = SelectField("FB og_type:", choices=[(t, t) for t in OG_TYPES])
    og_image = StringField("FB og_image:")
    # todo: fb_likes -- show as info with disabled field ??

    # english specific fields
    en_title = StringField("Title:")
    en_keywords = StringField("Keywords (meta):")
    en_description = StringField("Description (meta):")
    en_og_title = StringField("FB og_title:")
    en_og_description = StringField("FB og_description:")
    en_blog_cut = TextAreaField("Cut:")
    en_blog_text = TextAreaField("Text:")

    # russian specific fields
    ru_title = StringField(u"Тайтл:")
    ru_keywords = StringField(u"Кивордсы (meta):")
    ru_description = StringField(u"Дискрипшн (meta):")
    ru_og_title = StringField(u"FB ог_тайтл:")
    ru_og_description = StringField(u"FB ог_дискрипшн:")
    ru_blog_cut = TextAreaField(u"Вступление:")
    ru_blog_text = TextAreaField(u"Текст:")

    submit = SubmitField()

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
    og_type = SelectField("FB og_type:", choices=[(t, t) for t in OG_TYPES])
    og_image = StringField("FB og_image:")
    # todo: fb_likes -- show as info with disabled field ??

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
    ru_title = StringField(u"Тайтл:")
    ru_sub_title = StringField(u"Сабтайтл:")
    ru_keywords = StringField(u"Кивордсы (meta):")
    ru_description = TextAreaField(u"Дискрипшн (meta):")
    ru_og_title = StringField(u"FB ог_тайтл:")
    ru_og_description = TextAreaField(u"FB ог_дискрипшн:")
    ru_blog_cut = TextAreaField(u"Вступление:")
    ru_blog_text = TextAreaField(u"Текст:")

    # util fields
    submit = SubmitField()

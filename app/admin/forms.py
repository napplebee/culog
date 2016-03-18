from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import Required

class BlogPostForm(Form):
    # common fields
    name = StringField("Name (for internal purpose):")
    url = StringField("URL:")

    visible = BooleanField("Visible?")
    og_type = SelectField("FB og_type:")
    og_image = StringField("FB og_image:")
    # todo: fb_likes -- show as info with disabled field ??

    # english specific fields
    en_title = StringField("Title:")
    en_keywords = StringField("Keywords (meta):")
    en_description = StringField("Description (meta):")
    en_og_title = StringField("FB og_title:")
    en_og_description = StringField("FB og_description:")

    # russian specific fields
    ru_title = StringField("Title:")
    ru_keywords = StringField("Keywords (meta):")
    ru_description = StringField("Description (meta):")
    ru_og_title = StringField("FB og_title:")
    ru_og_description = StringField("FB og_description:")

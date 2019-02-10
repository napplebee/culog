# -*- coding: utf-8 -*-

import datetime as dt
from app.data.blog_posts import BlogPostHeader
from app.data.translations import Translation
from configs import Config as cfg

from app.core import db


class BlogPost(object):
    MULTI_LANG_FIELDS = ["title", "sub_title", "keywords", "description", "og_title", "og_description", "blog_cut", "blog_text"]
    id = None
    name = None
    url = None
    created_at = None
    published_at = None
    updated_at = None
    visible = None
    fb_likes = None

    title = None
    sub_title = None
    keywords = None
    description = None

    og_type = None
    og_image = None
    og_title = None
    og_description = None

    blog_cut = None
    blog_text = None

    fallback_chain = None
    base_url = None

    def __init__(self, fallback_chain, base_url):
        self.fallback_chain = fallback_chain
        self.base_url = base_url

    @staticmethod
    def populate_from_db(blog_header, lang_fallback=None, base_url=None):
        post = BlogPost(lang_fallback, base_url)
        post.id = blog_header.id
        post.name = blog_header.name
        post.url = blog_header.url
        post.created_at = blog_header.created_at
        post.published_at = blog_header.published_at
        post.updated_at = blog_header.updated_at
        post.visible = blog_header.visible
        post.fb_likes = blog_header.fb_likes

        post.og_type = blog_header.og_type
        post.og_image = blog_header.og_image

        post.title = {item.lang: item.value for item in blog_header.translations if item.name == "title"}
        post.sub_title = {item.lang: item.value for item in blog_header.translations if item.name == "sub_title"}
        post.keywords = {item.lang: item.value for item in blog_header.translations if item.name == "keywords"}
        post.description = {item.lang: item.value for item in blog_header.translations if item.name == "description"}

        post.og_title = {item.lang: item.value for item in blog_header.translations if item.name == "og_title"}
        post.og_description = {item.lang: item.value for item in blog_header.translations if item.name == "og_description"}

        post.blog_cut = {item.lang: item.value for item in blog_header.translations if item.name == "blog_cut"}
        post.blog_text = {item.lang: item.value for item in blog_header.translations if item.name == "blog_text"}

        return post

    @staticmethod
    def populate_from_ui(form, lang_fallback=None, base_url=None):
        post = BlogPost(lang_fallback, base_url)
        post.id = form.id.data
        post.name = form.name.data
        post.published_at = form.published_at.data
        post.url = form.url.data
        post.visible = form.visible.data
        post.og_type = form.og_type.data
        post.og_image = form.og_image.data

        for field in BlogPost.MULTI_LANG_FIELDS:
            value = {}
            for lang in cfg.SUPPORTED_LANGS:
                value[lang] = getattr(form, "{}_{}".format(lang, field)).data

            if len(value) > 0:
                setattr(post, field, value)

        return post

    def is_translated_for(self, lang):
        for field in BlogPost.MULTI_LANG_FIELDS:
            # print getattr(self, field)
            values = getattr(self, field)
            if lang not in values or values[lang] == "":
                return False
        return True

    def get_title(self):
        return self.__get_mlang_attr(self.title)

    def get_sub_title(self):
        return self.__get_mlang_attr(self.sub_title)

    def get_keywords(self):
        return self.__get_mlang_attr(self.keywords)

    def get_description(self):
        return self.__get_mlang_attr(self.description)

    def get_og_title(self):
        return self.__get_mlang_attr(self.og_title)

    def get_og_description(self):
        return self.__get_mlang_attr(self.og_description)

    def get_cut(self):
        return self.__get_mlang_attr(self.blog_cut)

    def get_text(self):
        return self.__get_mlang_attr(self.blog_text)

    def get_url(self):
        return "{0}/{1}".format(self.base_url, self.url)

    def __get_mlang_attr(self, attr):
        for lang in self.fallback_chain:
            if lang in attr and attr[lang]:
                return attr[lang]

        # raise ValueError("Can't find value for supported fallback chain")
        return ""

    def save(self):
        header = BlogPostHeader()

        header.name = self.name
        header.url = self.url
        header.created_at = dt.datetime.utcnow()
        header.published_at = self.published_at
        header.visible = self.visible
        header.fb_likes = self.fb_likes

        header.og_type = self.og_type
        header.og_image = self.og_image

        for field in BlogPost.MULTI_LANG_FIELDS:
            for lang in cfg.SUPPORTED_LANGS:
                t = Translation()
                t.name = field
                t.lang = lang
                t.value = getattr(self, field)[lang]
                t.created_at = dt.datetime.utcnow()
                header.translations.append(t)

        db.session.add(header)
        db.session.commit()
        return header.id
        # return header.id

    def update(self):
        header = BlogPostHeader.query.get(self.id)

        header.name = self.name
        header.url = self.url
        header.visible = self.visible
        # header.fb_likes = self.fb_likes

        header.og_type = self.og_type
        header.og_image = self.og_image
        header.published_at = self.published_at
        header.updated_at = dt.datetime.utcnow()

        for tr in header.translations:
            tr.value = getattr(self, tr.name)[tr.lang]
            tr.updated_at = dt.datetime.utcnow()

        db.session.commit()

    def __getattr__(self, item):
        for lang in cfg.SUPPORTED_LANGS:
            if item.startswith(lang):
                field_name = item[len(lang)+1:]
                if field_name in self.MULTI_LANG_FIELDS:
                    return getattr(self, field_name)[lang]

        raise AttributeError(item)

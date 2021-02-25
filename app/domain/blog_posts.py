# -*- coding: utf-8 -*-

import datetime as dt
from app.data.blog_posts import BlogPostHeader
from app.data.translations import Translation
from configs import Config as cfg
import duration as dr

from app.core import db


class BlogPost(object):
    MULTI_LANG_FIELDS = [
        "title", "sub_title", "keywords", "description", "og_title", "og_description", "blog_cut", "blog_text",
        "recipe_yield", "recipe_yield_number", "recipe_category", "recipe_cuisine"
    ]
    REQUIRED_TO_BE_TRANSLATED = [
        "title", "sub_title", "keywords", "description", "og_title", "og_description", "blog_cut", "blog_text",
        # "recipe_yield", "recipe_yield_number", "recipe_category", "recipe_cuisine"
    ]
    id = None
    name = None
    url = None
    created_at = None
    published_at = None
    updated_at = None
    visible = None
    is_article = None
    fb_likes = None

    cook_time = None
    prep_time = None

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

    recipe_yield = None
    recipe_yield_number = None
    recipe_category = None
    recipe_cuisine = None

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
        post.is_article = blog_header.is_article
        post.fb_likes = blog_header.fb_likes

        post.cook_time = blog_header.cook_time
        post.prep_time = blog_header.prep_time

        post.og_type = blog_header.og_type
        post.og_image = blog_header.og_image

        #add here a few lines for a new field
        post.title = {item.lang: item.value for item in blog_header.translations if item.name == "title"}
        post.sub_title = {item.lang: item.value for item in blog_header.translations if item.name == "sub_title"}
        post.keywords = {item.lang: item.value for item in blog_header.translations if item.name == "keywords"}
        post.description = {item.lang: item.value for item in blog_header.translations if item.name == "description"}

        post.og_title = {item.lang: item.value for item in blog_header.translations if item.name == "og_title"}
        post.og_description = {item.lang: item.value for item in blog_header.translations if item.name == "og_description"}

        post.blog_cut = {item.lang: item.value for item in blog_header.translations if item.name == "blog_cut"}
        post.blog_text = {item.lang: item.value for item in blog_header.translations if item.name == "blog_text"}

        post.recipe_yield = {item.lang: item.value for item in blog_header.translations if item.name == "recipe_yield"}
        post.recipe_yield_number = {item.lang: item.value for item in blog_header.translations if item.name == "recipe_yield_number"}
        post.recipe_category = {item.lang: item.value for item in blog_header.translations if item.name == "recipe_category"}
        post.recipe_cuisine = {item.lang: item.value for item in blog_header.translations if item.name == "recipe_cuisine"}

        return post

    @staticmethod
    def populate_from_ui(form, lang_fallback=None, base_url=None):
        post = BlogPost(lang_fallback, base_url)
        post.id = form.id.data
        post.name = form.name.data
        post.published_at = form.published_at.data
        post.url = form.url.data
        post.visible = form.visible.data
        post.is_article = form.is_article.data
        post.og_type = form.og_type.data
        post.og_image = form.og_image.data

        post.cook_time = form.cook_time.data
        post.prep_time = form.prep_time.data

        for field in BlogPost.MULTI_LANG_FIELDS:
            value = {}
            for lang in cfg.SUPPORTED_LANGS:
                value[lang] = getattr(form, "{}_{}".format(lang, field)).data

            if len(value) > 0:
                setattr(post, field, value)

        return post

    def is_translated_for(self, lang):
        for field in BlogPost.REQUIRED_TO_BE_TRANSLATED:
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

    def get_recipe_yield(self):
        return self.__get_mlang_attr(self.recipe_yield)

    def get_recipe_yield_number(self):
        return self.__get_mlang_attr(self.recipe_yield_number)

    def get_recipe_category(self):
        return self.__get_mlang_attr(self.recipe_category)

    def get_recipe_cuisine(self):
        return self.__get_mlang_attr(self.recipe_cuisine)

    def get_url(self):
        return "{0}/{1}".format(self.base_url, self.url)

    def get_cook_time_iso(self):
        if self.cook_time is None or self.cook_time == "":
            return ""
        return dr.to_iso8601(str(self.cook_time), strict=False)

    def get_cook_time_ui(self, lang):
        if self.cook_time is None or self.cook_time == "":
            return ""
        return self._get_lang_aware_time(dr.to_tuple(str(self.cook_time), strict=False), lang)

    def get_prep_time_iso(self):
        if self.prep_time is None or self.prep_time == "":
            return ""
        return dr.to_iso8601(str(self.prep_time), strict=False)

    def get_prep_time_ui(self, lang):
        if self.prep_time is None or self.prep_time == "":
            return ""
        return self._get_lang_aware_time(dr.to_tuple(str(self.prep_time), strict=False), lang)

    def get_total_time_iso(self):
        if (self.cook_time is None and self.prep_time is None) or \
                (self.cook_time == "" and self.prep_time == ""):
            return ""
        cook_delta = dr.to_timedelta(str(self.cook_time if self.cook_time is not None else "0:0"), strict=False)
        prep_delta = dr.to_timedelta(str(self.prep_time if self.prep_time is not None else "0:0"), strict=False)
        return dr.to_iso8601(cook_delta + prep_delta, strict=False)

    def _get_lang_aware_time(self, time_tuple, lang):
        if len(time_tuple) != 3: return "--"
        hh, mm, ss = time_tuple
        result = u""
        delim = u""
        if lang == u"ru":
            if hh != 0:
                result = u"{0} ч.".format(hh)
                delim = u" "
            if mm != 0:
                result = u"{0}{1}{2} мин.".format(result, delim, mm)
        elif lang == u"en":
            if hh != 0:
                result = u"{0} h.".format(hh)
                delim = u" "
            if mm != 0:
                result = u"{0}{1}{2} min.".format(result, delim, mm)
        return result

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
        header.is_article = self.is_article
        header.fb_likes = self.fb_likes

        header.og_type = self.og_type
        header.og_image = self.og_image

        header.cook_time = self.cook_time
        header.prep_time = self.prep_time

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

    def update(self):
        header = BlogPostHeader.query.get(self.id)

        header.name = self.name
        header.url = self.url
        header.visible = self.visible
        header.is_article = self.is_article
        # header.fb_likes = self.fb_likes

        header.cook_time = self.cook_time
        header.prep_time = self.prep_time

        header.og_type = self.og_type
        header.og_image = self.og_image
        header.published_at = self.published_at
        header.updated_at = dt.datetime.utcnow()

        # todo: add new translations

        possible_translations = list(BlogPost.MULTI_LANG_FIELDS)

        # at this point there are might be new translations we need to add
        # For instance if we created a new post with 2 translatable fields (f1, f2) and set of translations A (t1, t2),
        # then we added new translatable field (f3) but all existing posts are not aware
        # about newly created f3. Then when we update any existing
        # post we need to update t1, t2 and create t3
        for tr in header.translations:
            multilang_value = getattr(self, tr.name)
            if multilang_value is not None:
                tr.value = multilang_value[tr.lang]
                tr.updated_at = dt.datetime.utcnow()
                # there are two translations with the same name for RU & EN
                if tr.name in possible_translations:
                    possible_translations.remove(tr.name)

        # now it's time to handle "new" translatable fields
        for tr_name in possible_translations:
            multilang_value = getattr(self, tr_name)
            for lang in cfg.SUPPORTED_LANGS:
                t = Translation()
                t.name = tr_name
                t.lang = lang
                t.value = multilang_value[lang]
                t.created_at = dt.datetime.utcnow()
                header.translations.append(t)
        db.session.commit()

    def __getattr__(self, item):
        for lang in cfg.SUPPORTED_LANGS:
            if item.startswith(lang):
                field_name = item[len(lang)+1:]
                if field_name in self.MULTI_LANG_FIELDS:
                    return getattr(self, field_name)[lang]

        raise AttributeError(item)

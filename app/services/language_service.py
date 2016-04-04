# -*- coding: utf-8 -*-

from itertools import dropwhile


class LanguageService(object):

    def get_user_settings(self, preferred_lang=None):
        lang_fallback = ["en"]
        current_lang = "en"

        if preferred_lang is not None:
            # in case when fallback_chain = [es-br, es, en] and preferred_lang == es
            lang_fallback = list(dropwhile(lambda lng: lng != preferred_lang, lang_fallback))
            if len(lang_fallback) == 0:
                # default fallback_chain, e.g. fallback_chain = [es-br, es, en] and preferred_lang == ru
                lang_fallback = [preferred_lang, "en"]

        return current_lang, lang_fallback


langService = LanguageService()

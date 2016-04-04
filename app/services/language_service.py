# -*- coding: utf-8 -*-

from itertools import dropwhile


class LanguageService(object):

    def get_user_settings(self, request, lang_override=None):
        preferred_lang = lang_override if lang_override is not None else request.cookies.get("lang", "en")
        if preferred_lang == "ru":
            return preferred_lang, ["ru", "en"]
        else:
            return preferred_lang, ["en"]


langService = LanguageService()

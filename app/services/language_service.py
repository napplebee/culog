# -*- coding: utf-8 -*-

class LanguageService(object):

    def get_user_settings(self, request, lang_override=None):
        preferred_lang = lang_override if lang_override is not None else request.cookies.get("lang", "en")
        if preferred_lang == "ru":
            return preferred_lang, ["ru", "en"]
        else:
            return preferred_lang, ["en"]

        # lang_fallback = ["en"]
        # current_lang = preferred_lang
        # in case when fallback_chain = [es-br, es, en] and preferred_lang == es
        # lang_fallback = list(dropwhile(lambda lng: lng != preferred_lang, lang_fallback))
        # if len(lang_fallback) == 0:
        #     # default fallback_chain, e.g. fallback_chain = [es-br, es, en] and preferred_lang == ru
        #     lang_fallback = [preferred_lang, "en"]

        # return current_lang, lang_fallback


langService = LanguageService()

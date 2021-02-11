# -*- coding: utf-8 -*-

class Phrase(object):
    about = None
    recipes = None
    recent_recipes = None
    categories = None
    you_may_like = None
    reserved_rights = None
    load_more = None

    def __init__(self, about, recipes, recent_recipes, categories, you_may_like, reserved_rights, load_more):
        self.about = about
        self.recipes = recipes
        self.recent_recipes = recent_recipes
        self.categories = categories
        self.you_may_like = you_may_like
        self.reserved_rights = reserved_rights
        self.load_more = load_more


PHRASES = {
    "ru": Phrase(u"Обо мне", u"Рецепты", u"Недавние рецепты", u"Категории", u"Вам может понравится", u"Все права защищены", u"Показать еще"),
    "en": Phrase(u"About", u"Recipes", u"Recent recipes", u"Categories", u"You may like", u"All rights reserved", u"Load more")
}

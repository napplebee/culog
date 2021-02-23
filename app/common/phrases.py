# -*- coding: utf-8 -*-

class Phrase(object):
    about = None
    recipes = None
    recent_recipes = None
    categories = None
    you_may_like = None
    reserved_rights = None
    load_more = None
    read_more = None
    ingredients = None
    process = None

    def __init__(self, about, recipes, recent_recipes,
                 categories, you_may_like, reserved_rights,
                 ingredients, process, load_more, read_more, amount_types):
        self.about = about
        self.recipes = recipes
        self.recent_recipes = recent_recipes
        self.categories = categories
        self.you_may_like = you_may_like
        self.reserved_rights = reserved_rights
        self.ingredients = ingredients
        self.process = process
        self.load_more = load_more
        self.read_more = read_more
        self.amount_types = amount_types


PHRASES = {
    "ru": Phrase(u"Обо мне", u"Рецепты", u"Недавние рецепты", u"Категории", u"Вам может понравится", u"Все права защищены",
         u"Ингредиенты", u"Процесс", u"Показать еще", u"читать дальше",
         {"gr": "гр.", "ml": "мл.", "item": "", "tsp": "ч.л.", "tbsp": "ст.л.", "cup": "стакана", "kg": "кг.", "liter": "л."}
     ),
    "en": Phrase(u"About", u"Recipes", u"Recent recipes", u"Categories", u"You may like", u"All rights reserved",
        u"Ingredients", u"Process", u"Load more", u"read now",
        {"gr": "g", "ml": "ml", "item": "", "tsp": "tsp", "tbsp": "tbsp", "cup": "cup", "kg": "kg", "liter": "l"}
     )
}
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
    preparation_time = None
    cooking_time = None
    total_time = None
    cuisine = None
    category = None
    recipe_yield = None
    published = None
    updated = None
    calories = None
    proteins = None
    fats = None
    carbs = None
    process = None
    optional = None
    amount_types = None

    def __init__(self, about, recipes, recent_recipes,
                 categories, you_may_like, reserved_rights,
                 ingredients, process, load_more, read_more,
                 preparation_time, cooking_time, total_time,
                 cuisine, category, recipe_yield, published,
                 updated, calories, proteins, fats, carbs,
                 optional,
                 amount_types):
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
        self.preparation_time = preparation_time
        self.cooking_time = cooking_time
        self.total_time = total_time
        self.cuisine = cuisine
        self.category = category
        self.recipe_yield = recipe_yield
        self.published = published
        self.updated = updated
        self.calories = calories
        self.proteins = proteins
        self.fats = fats
        self.carbs = carbs
        self.optional = optional
        self.amount_types = amount_types


PHRASES = {
    "ru": Phrase(u"Обо мне", u"Рецепты", u"Недавние рецепты", u"Категории", u"Вам может понравится", u"Все права защищены",
         u"Ингредиенты", u"Процесс", u"Показать еще", u"читать дальше", u"Время подготовки", u"Время приготовления",
         u"Суммарное время", u"Кухня", u"Блюдо", u"Число порций", u"Опубликовано", u"обновлено", u"Калорийность",
         u"Белки", u"Жиры", u"Углеводы", u"необязательно",
         {"gr": "г", "ml": "мл.", "item": "", "tsp": "ч.л.", "tbsp": "ст.л.", "cup": "стакана", "kg": "кг", "liter": "л."}
     ),
    "en": Phrase(u"About", u"Recipes", u"Recent recipes", u"Categories", u"You may like", u"All rights reserved",
        u"Ingredients", u"Process", u"Load more", u"read now", u"Preparation time", u"Cooking time",
         u"Total time", u"Cuisine", u"Category", u"Recipe yield", u"Published", u"updated", u"Calories",
         u"Proteins", u"Fats", u"Carbs", u"optional",
        {"gr": "g", "ml": "ml", "item": "", "tsp": "tsp", "tbsp": "tbsp", "cup": "cup", "kg": "kg", "liter": "l"}
     )
}

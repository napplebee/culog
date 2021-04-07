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
    default_title = None
    default_og_description = None
    default_keywords = None
    categories_title = None
    categories_description = None
    categories_og_description = None
    categories_keywords = None
    amount_types = None

    def __init__(self, about, recipes, recent_recipes,
                 categories, you_may_like, reserved_rights,
                 ingredients, process, load_more, read_more,
                 preparation_time, cooking_time, total_time,
                 cuisine, category, recipe_yield, published,
                 updated, calories, proteins, fats, carbs,
                 optional, default_title, default_og_description, 
                 default_keywords, categories_title, 
                 categories_description, categories_og_description, 
                 categories_keywords, amount_types):
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
        self.default_title = default_title
        self.default_og_description = default_og_description
        self.default_keywords = default_keywords
        self.categories_title = categories_title
        self.categories_description = categories_description
        self.categories_og_description = categories_og_description
        self.categories_keywords = categories_keywords
        self.amount_types = amount_types


PHRASES = {
    "ru": Phrase(u"Обо мне", u"Рецепты", u"Недавние рецепты", u"Категории", u"Вам может понравится", u"Все права защищены",
        u"Ингредиенты", u"Процесс", u"Показать еще", u"читать дальше", u"Время подготовки", u"Время приготовления",
        u"Суммарное время", u"Кухня", u"Блюдо", u"Число порций", u"Опубликовано", u"обновлено", u"Калорийность",
        u"Белки", u"Жиры", u"Углеводы", u"необязательно", u"Cook With Love: семейные рецепты",
        u"За каждым рецептом стоит история. Я собираю такие истории и делюсь ими в этом блоге. Хотите рассказать свою?",
        u"пошаговые рецепты домашние, домашние пошаговые фото рецепты, рецепты с фото пошагово, cook with love, фуд блог, домашные рецепты, семейные рецепты, простые рецепты, вкусные блюда",
        {"завтрак": "Рецепты завтраков",
        "салат": "Рецепты салатов",
        "гарнир": "Рецепты гарниров",
        "основное блюдо": "Рецепты основных блюд",
        "сливочный сыр": "Рецепты сливочного сыра",
        "закуска": "Рецепты закусок",
        "десерт": "Рецепты десертов"
        },
        {"завтрак": """<p>Рецепты завтраков могут быть самыми разными, но все сходятся в одном: завтрак - важный прием пищи. Завтрак не только заряжает энергией, но и может задать настроение на весь день, так что про вкус и вид тоже не стоит забывать. Безусловно, чаще всего приготовление завтрака должно быть быстрым, но иногда можно потратить чуть больше времени и приготовить что-то особенное.</p>
            <p>В этом разделе я постаралась собрать рецепты приготовления завтраков, пусть и не самых простых, но, в то же время, удивительно вкусных.</p>""",
         "салат": """<p>Салаты могут быть разными - мясными, овощными, рыбными, фруктовыми… Все рецепты салатов не перечислить, ингредиенты легко можно менять тем самым создавая бесконечное число вариантов. Вспомните оливье: кто-то добавляет горошек, кто-то нет, кто-то любит мясо или говяжий язык, а кто-то предпочитает салат с курицей, некоторые любят свежие огурцы, а некоторые предпочитают соленые, а еще есть оливье с яблоком, вы знали? И все это разные блюда!</p>
            <p>Готовя салат не стоит забывать о заправке. Салат с майонезом это отличный вариант, но иногда хочется чего-то более легкого - добавьте оливковое масло, оно прекрасно сгладит резкий и насыщенный вкус других ингредиентов,  например, руколы. А если вам хочется добавить ореховое послевкусие - добавьте кунжутное или ореховое масло. Заправка для салата будет не полной без легкой кислинки - с этой задачей справится сок цитрусовых или уксус. Подробнее про заправки для салатов можно почитать в <a href="/ru/article/salad_dressing_and_vinaigrette" target="_blank">этом посте</a>.</p>
            <p>Придумывая необычный рецепт салата, включите фантазию! Расскажу как это делаю я. Хочется чего-то сытного - приготовим салат с мясом, возьмем говяжий язык, он прекрасно сочетается с чем-нибудь остреньким. Можно, конечно, добавить остроты в заправку для салата, например, горчицу, но хочется что-то интересное, что-то, что добавит текстуры и цвета - возьмем руколу. Пряность руколы и жесткость листьев отлично сгладит что-то сочное и сладкое, для этого подойдет апельсин, главное, очистить его от пленок. Сладость хочется приглушить чем-то соленым - хлопья пармезана или другого старого сыра точно справятся с этой задачей. Пока получается не слишком сбалансированно - многовато тяжелых ингредиентов, положим чуть больше руколы и разбавим ее насыщенный вкус авокадо или помидорами черри с моцареллой или листьями салата айсберг. Плотная, нежная мякоть авокадо и листья салата айсберг не только добавят еще больше красок, но и сбалансируют салат, выберу их. Ура! Салат готов! А что с заправкой? Салат очень насыщенный, сытный и яркий, а значит заправка должна быть легкой, нейтрального цвета, с кислинкой. Чтобы не испортить внешний вид - откажемся от  бальзамического уксуса. Легкую кислинку добавит лимонный сок, он так же сгладит сладость апельсина и не даст авокадо потемнеть. Масло возьмем максимально нейтральное, чтобы сочеталось со слабой кислотой - оливковое. Все ингредиенты для заправки в банку, добавим немного соли, встряхнем и вуаля, салат готов!</p>
            <p>В этом разделе я постаралась собрать рецепты моих любимых салатов. Они очень разные, есть сытные с мясом, есть легкие с ягодами, есть классические. Надеюсь салаты, приготовленные по этим рецептам, вам понравятся или, как минимум, вдохновят вас на создание собственных рецептов.</p>""",
        "гарнир": """<p>С одной стороны гарнир это всего лишь дополнение к основному блюду, а с другой - это то, что позволит вам превратить любой, даже самый простой, прием пищи в нечто особенное. Попробуйте заметить привычную картошку пюре поджаренными в духовке ломтиками картошки, заправьте макароны соусом песто и украсьте половинками помидорок черри, или просто отварите рис в бульоне вместо воды. Если вы готовы к экспериментам, замените рис на киноа или булгур, попробуйте макароны из бобовых или гречневую лапшу. Ведь не зря слово гарнир происходит от французского garnir - снабжать, украшать. Пусть ваши основные блюда украсят необычные гарниры, не бойтесь экспериментировать!</p>
            <p>В этом разделе я постараюсь собрать свои любимые рецепты гарниров, которые, я надеюсь, понравятся и вам.</p>""",
        "основное блюдо": """<p>Основные блюда занимают особенное место в жизни большинства людей. Основные блюда могут быть из мяса и птицы, могут быть вегетарианскими и веганскими - просто включите фантазию!</p>
            <p>Когда я вспоминаю детство, в голове всплывают воспоминания о шашлыках, на которые мы ходили всей семьей, воспоминания о том, как я впервые попробовала мясо по-французски в первом классе на дне рождении школьной подруги, о том, как бабушка готовила котлеты, а мама жарила рыбу…</p>
            <p>Мясо и рыбу для основного блюда можно обжаривать, запекать, тушить и даже есть в сыром виде, вспомните тартар. Главное обращайте внимание на температурный режим, например, не все виды мяса стоит готовить как стейк с кровью и использовать для тартара, больше про температуру приготовления вы найдете в <a href="/ru/other/cooking_temperatures" target="_blank">этой статье</a>.</p>
            <p>В этом разделе я буду собрать свои любимые рецепты основных блюд. Надеюсь пошаговые рецепты с фото помогут вам приготовить идеальное основное блюдо.</p>""",
        "сливочный сыр": """<p>Сливочный сыр мягкий, сладкий, с легким вкусом молока и сливок. Этот сыр имеет нежную консистенцию, не требует созревания и этим отличается от других сыров. Такой сыр очень легко приготовить дома, он идеален для десертов и сливочных кремов. А если добавить немного соли и рубленой зелени, он прекрасно подойдет в качестве начинки для <a href="/ru/breakfast/carrot_crepes" target="_blank">морковных блинчиков</a>, а так же он прекрасно сочетается с <a href="/ru/appetizer/mediterranean_salmon_gravlax" target="_blank">соленым лососем</a>.</p>
            <p>В этом разделе вы найдете простые рецепты сливочного сыра с подробным описанием и фотографиями процесса приготовления. Приятного аппетита!</p>""",
        "закуска": """<p>Закуски это особенная категория блюд, чаще всего они подаются перед основным приемом пищи, но могут выступать в качестве самостоятельного легкого перекуса. Закуски должны пробуждать аппетит, готовить к будущей трапезе и задавать настроение.</p>
            <p>Рецептов закусок много: от простых повседневных, которые готовятся очень быстро, до сложных и изысканных, приготовление которых легко может занять часы. Закуски могут быть горячими и холодными, они могут быть мясными, рыбными, овощными и фруктовыми.</p>
            <p>В этом разделе я собираю свои любимые закуски, тут нет случайных, скучных и непроверенных рецептов. Надеюсь, фото и пошаговые рецепты облегчат процесс приготовления.</p>""",
        "десерт": """<p>Когда все основные блюда уже убраны со стола и чай уже заварен, наступает время финального сладкого аккорда - время десерта. Выбор практически безграничен, а рецептов десертов даже больше чем их названий, в каждой стране вы найдете национальные сладости, а в каждой семье есть любимый домашний десерт. Вспомните, какой ваш любимый десерт?</p>
            <p>Для меня десерт это один из способов порадовать родных и близких, сделать утро коллег чуть более солнечным, а долгие зимние вечера чуть более уютными. Согласитесь, запах свежей выпечки великолепен, и не важно настигает ли он вас, когда вы проходите мимо пекарни или когда вы заходите домой. Но десерты это не только выпечка - это еще и разнообразные муссы, желе, суфле и мороженое. И не смотря на такое разнообразие, я обожаю выпечку.</p>
            <p>Каждый раз придумывая десерт, смешивая ингредиенты, я думаю о том, кто будет его есть, о том, каким будет основное блюдо, о том, какой напиток будет рядом. Латте или капучино будет прекрасно сочетаться с <a href="/ru/baking/caramel_brownies" target="_blank">брауни</a>, чай с <a href="/ru/baking/moist_lemon_cake" target="_blank">лимонным кексом</a>, а стакан теплого молока с <a href="/ru/baking/cottage_cheese_casserole_with_apples_and_cashew" target="_blank">творожной запеканкой</a>.</p>
            <p>В этом разделе собраны мои любимые рецепты десертов. Тут вы найдете не только пошаговые рецепты и фото готовых десертов, но и мои заметки, которые, я надеюсь, помогут вам в их приготовлении.</p>"""
        },
        {"завтрак": "Рецепты вкусных и необычных завтраков с пошаговыми инструкциями и фото.",
        "салат": "Рецепты вкусных и необычных салатов с пошаговыми инструкциями и фото.",
        "гарнир": "Рецепты вкусных и необычных гарниров с пошаговыми инструкциями и фото.",
        "основное блюдо": "Рецепты вкусных и необычных основных блюд с пошаговыми инструкциями и фото.",
        "сливочный сыр": "Рецепты вкуснейшего сливочного сыра с пошаговыми инструкциями и фото.",
        "закуска": "Рецепты вкусных и необычных закусок с пошаговыми инструкциями и фото.",
        "десерт": "Рецепты вкусных и необычных десертов с пошаговыми инструкциями и фото."},
        {"завтрак": "рецепты завтраков, завтрак рецепты, вкусные завтраки рецепты, рецепты завтраков с фото, завтрак рецепты простые, вкусный завтрак",
        "салат": "рецепты салатов, салат рецепт классический, салаты рецепты с фото, вкусные салаты рецепты, простые рецепты салатов, рецепт салата с курицей, рецепты салатов простые и вкусные, вкусные салаты рецепты с фото, вкусный рецепт, легкий салат",
        "гарнир": "рецепты гарниров, гарниры рецепты, гарниры рецепты приготовления, вкусные гарниры рецепты, рецепты гарниров простые",
        "основное блюдо": "рецепты основных блюд, праздничное основное блюдо рецепты, вкусный рецепт основного блюда, мясо в духовке рецепты, мясо рецепты с фото, рецепты из мяса, рецепт мяса пошагово, мясо блюдо, рецепты из курицы, курица рецепты с фото, домашняя курица рецепты",
        "сливочный сыр": "рецепты сливочного сыра, сливочный сыр, сливочный сыр рецепт, сыр творожный сливочный, сливочный сыр для крема, сливочный сыр для торта, домашний сливочный сыр, домашний сыр, сыр приготовление, сливочный сыр рецепт с фото, домашний сливочный сыр рецепт, сыр домашний рецепт, сыр творог рецепт",
        "закуска": "рецепты закусок, закуски рецепты с фото, праздничные закуски рецепты, закуски на стол рецепты, закуски на праздничный стол рецепты, простые рецепты закусок, рецепты вкусных закусок, холодная закуска, стол закуска, закуска фото, праздничный стол закуска",
        "десерт": "рецепты десертов, десерты рецепты с фото, простые рецепты десертов, десерты рецепты в домашних условиях, торт рецепт, фото рецепт, десерты рецепты простые и вкусные, десерты рецепты пошагово, рецепты десертов фото пошагово, выпечка десерты, вкусные десерты, десерты фото, домашние десерты"},
        {"gr": "г", "ml": "мл.", "item": "", "tsp": "ч.л.", "tbsp": "ст.л.", "cup": "стакана", "kg": "кг", "liter": "л."}
     ),
    "en": Phrase(u"About", u"Recipes", u"Recent recipes", u"Categories", u"You may like", u"All rights reserved",
         u"Ingredients", u"Process", u"Load more", u"read now", u"Preparation time", u"Cooking time",
         u"Total time", u"Cuisine", u"Category", u"Recipe yield", u"Published", u"updated", u"Calories",
         u"Proteins", u"Fats", u"Carbs", u"optional", u"Cook With Love: food blog",
         u"Each and every recipe has a story behind it. I'm collecting family recipes that are full love and warm memories. Do you have one?",
         u"food blog, easy recipes, home cooking, cooking, recipes, baking, dessert recipes, homecooking, yummy recipes, cook with love",
        {"breakfast": "Breakfast recipes",
         "salad": "Salad recipes",
         "side dish": "Side dish recipes",
         "dinner": "Dinner and main cource recipes",
         "cream cheese": "Cream cheese recipes",
         "appetizer": "Appetizer recipes",
         "dessert": "Dessert recipes"
        },
        {"breakfast": """<p>Breakfast recipes can be very different, but they all agree on one thing: breakfast is an important meal. Breakfast not only energizes you, but it can also set the mood for the whole day, so you shouldn't forget about taste and appearance. Of course, more often than not, breakfast should be prepared quickly, but sometimes you can spend a little more time and cook something special.</p>
            <p>In this section, I’ve tried to collect recipes for making breakfasts; they aren’t the most simple ones, but surprisingly tasty. </p>""",
         "salad":"""<p>Salads can be different - meat, vegetable, fish, fruit… It’s impossible to list all the salad recipes, the ingredients can be easily changed, thereby you can create an infinite number of options. Remember Olivier: some people add peas, some people don’t; some people love meat or beef tongue, others prefer a salad with chicken; some people like fresh cucumbers, others prefer pickles; there’s also Olivier with apples, did you know? And all these are different dishes!</p>
            <p>When preparing a salad, don’t forget about a dressing. Mayonnaise salad is a great option, but sometimes you may want something lighter - then add olive oil, it perfectly smoothes the rich taste of other ingredients such as, for example, arugula. And if you want to add a nutty aftertaste - add sesame or walnut oil. A salad dressing would be incomplete without a slight sourness - citrus juice or vinegar can cope with this task. You can read more about salad dressings in <a href="/en/article/salad_dressing_and_vinaigrette" target="_blank">here</a>.</p>
            <p>When coming up with an unusual salad recipe, turn on your imagination! I'll tell you how I do it. If you want something hearty - then prepare a salad with meat, take a beef tongue, it goes well with something spicy. You can, of course, add spice to a salad dressing, such as mustard, but sometimes you may want something interesting, something that adds texture and color - let’s take the arugula. The spice of arugula and the hardness of the leaves can perfectly smooth something juicy and sweet; an orange is suitable for this, the main thing is to peel it. I want to dilute the sweetness with something salty - so I take Parmesan or any other long-aged cheese, they will definitely cope with this task. It’s still not balanced enough - there are too many heavy ingredients, let’s put a little more arugula and dilute its rich taste with avocado, or cherry tomatoes with mozzarella, or iceberg lettuce. Thick, tender avocado flesh and iceberg lettuce don’t only add even more colors, but they also balance the salad, so I choose this option. Hooray! The salad is ready!</p>
            <p>But what about a salad dressing? The salad is very rich, hearty and bright, which means that the dressing should be light, neutral in color, with sourness. In order not to spoil the appearance - we won’t use balsamic vinegar. Lemon juice will add a slight sourness, it will also smooth the sweetness of the orange and prevent the avocado from darkening. We take the oil as neutral as possible so that it’s combined with a weak acid - an olive one. We put all the ingredients for dressing in a jar, add a little salt, shake and voila, the salad is ready!</p>
            <p>In this section, I’ve tried to collect recipes for making my favorite salads. They are very different: there are hearty ones with meat, there are light ones with berries, there are classic ones. I hope you’ll enjoy the salads made according to these recipes or, at least, they’ll inspire you to create your own recipes.</p>""",
         "side dish": """<p>On the one hand, a side dish is just an addition to the main course, but on the other hand, it is something that will allow you to turn any, even the simplest, a meal into something special. Replace your usual mashed potatoes with baked potato slices, add pesto to pasta and decorate it with halved cherry tomatoes, or just boil rice in broth instead of water. If you're ready to experiment, replace rice with quinoa or bulgur, try bean pasta or buckwheat noodles. Brighten your main course with an unusual side dish, don't be afraid to experiment!</p>
            <p>In this section, I’ve tried to collect my favorite side dish recipes, which I hope you will also like.</p>""",
         "dinner": """<p>Dinners have a special place in most people's lives. Main dishes for dinners can be meat and poultry, vegetarian or vegan - just get creative!</p>
            <p>When I think about my childhood, I remember the barbecue that I had with my family; I also remember how I first tried Veal Orloff at the birthday of my school friend; I remember how my grandmother cooked chops and my mother fried fish…</p>
            <p>Meat and fish for the main course can be fried, baked, stewed and even eaten raw, (remember tartare). The main thing is to pay attention to the temperature regime, for example, not all types of meat should be cooked like a rare steak and used for tartare. You will find more about the cooking temperature in <a href="/en/other/cooking_temperatures" target="_blank">this article</a>. 
            <p>In this section, I will collect my favorite main course recipes. I hope the step-by-step picture recipes will help you prepare the perfect main course.</p>""",
         "cream cheese": """<p>Cream cheese is soft, sweet, with a light taste of milk and cream. This cheese has a tender texture, doesn’t require ripening, and thus differs from other cheeses. This cheese is very easy to make at home, it’s ideal for desserts and buttercreams. And if you add a little salt and chopped herbs, it is perfect as a filling for carrot pancakes, and it also goes well with the salted salmon.</p>
            <p>In this section, you will find simple step-by-step picture recipes for cream cheese with detailed descriptions. Enjoy your meal!</p>""",
         "appetizer": """<p>Appetizers are a special category of dishes, most often they are served before the main meal, but can act as an independent light snack. Appetizers should whet your appetite, prepare for future meals, and set the mood. There are many recipes for appetizers: from simple everyday ones that are prepared very quickly, to complicated and sophisticated ones, which can take hours to prepare. Appetizers can be hot and cold, they can be meat, fish, vegetable, and fruit.</p>
            <p>In this section, I collect my favorite appetizer recipes, there are no random, boring, and untested recipes here. I hope the step-by-step picture recipes will make the cooking process easier.</p>""",
         "dessert": """<p>When all the main dishes have already been removed from the table and tea has already been made, it is time for the final sweet accord - the time for dessert. The choice is almost limitless: in every country you will find national sweets, and every family has a favorite homemade dessert. Remember what is your favorite dessert?</p>
            <p>For me, dessert is one of the ways to please family and friends, to make colleagues' mornings a little more sunny, and long winter evenings a little more cozy. Agree, the smell of fresh baked goods is great, and it doesn't matter if you feel it when you walk by the bakery or when you come home. But desserts are not only baked goods - they are also a variety of mousses, jellies, soufflés and ice cream. And despite this variety, I love baked goods.</p>
            <p>Every time I come up with a dessert, I mix the ingredients, thinking about who will eat it, what the main course will be, what the drink will be served. Latte or cappuccino goes well with a brownie, tea with a lemon muffin, and a glass of warm milk with a curd casserole.</p>
            <p>This section contains my favorite dessert recipes. Here you will find not only step-by-step picture recipes of ready-made desserts, but also my notes, which, I hope, will help you to prepare them.</p>"""},
        {"breakfast":"Explore loads of delicious breakfast recipes to start your morning off right.",
         "salad": "Explore loads of yummy and colorful salad recipes here.",
         "side dish": "Explore delicious side dish recipes that will compliment your best main dishes.",
         "dinner": "Explore loads of delicious main course recipes for the best dinner parties.",
         "cream cheese": "Explore healthy and delicious cream cheese recipes.",
         "appetizer": "Explore delicious appetizer recipes to start your dinner or party off right.",
         "dessert": "Explore loads of delicious dessert recipes to sweeten your day."},
        {"breakfast":"breakfast, breakfast recipes, breakfast ideas, breakfast food, morning food, breakfast appliances, easy breakfast recipes, healthy breakfast recipes, quick breakfast recipes, easy healthy breakfasts, savoury breakfast, sweet breakfast",
         "salad": "salad recipe, broccoli salad, chicken salad, salad recipes, spinach salad, antipasto salad, main salad, side salad, tuna salad, vegetarian, vegetarian salad",
         "side dish": "side dish recipes, side dish ideas, vegetable side dish, side dish for fish,  side dish for meat, summer side dish recipe, holiday side dish recipe, vegetable side dish recipe",
         "dinner": "main recipe, main course recipe, dinner recipe, lunch recipe",
         "cream cheese": "cream cheese recipes, how to make cream cheese, cream cheese dip, cream cheese nutrition, cream cheese desserts, philadelphia cream cheese recipes",
         "appetizer": "appetizer recipe, appetizer recipes, appetizer ideas, appetizer, best appetizer recipes, easy appetizer recipes, easy appetizer ideas, cold appetizer recipes, hot appetizer recipes",
         "dessert": "dessert recipe, dessert recipes, dessert, easy dessert recipes, dessert ideas, apple dessert recipes, best dessert recipes, dessert food, easy dessert, apple dessert, lemon dessert recipes, easy dessert recipes with few ingredients, dessert gallery"},
        {"gr": "g", "ml": "ml", "item": "", "tsp": "tsp", "tbsp": "tbsp", "cup": "cup", "kg": "kg", "liter": "l"}
     )
}

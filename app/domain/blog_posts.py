from configs import Config as cfg


class BlogPost(object):
    name = None
    url = None
    created_at = None
    updated_at = None
    visible = None
    fb_likes = None

    title = None
    keywords = None
    description = None

    og_type = None
    og_image = None
    og_title = None
    og_description = None

    @staticmethod
    def populate_from_db(blog_header):
        post = BlogPost()
        post.name = blog_header.name
        post.url = blog_header.url
        post.created_at = blog_header.created_at
        post.updated_at = blog_header.updated_at
        post.visible = blog_header.visible
        post.fb_likes = blog_header.fb_likes

        post.title = {item.lang: item.value for item in blog_header.translations if item.name == "title"}
        post.keywords = {item.lang: item.value for item in blog_header.translations if item.name == "keywords"}
        post.description = {item.lang: item.value for item in blog_header.translations if item.name == "description"}

        post.og_type = blog_header.og_type
        post.og_image = blog_header.og_image
        post.og_title = {item.lang: item.value for item in blog_header.translations if item.name == "og_title"}
        post.og_description = {item.lang: item.value for item in blog_header.translations if item.name == "og_description"}

        post.blog_cut = {item.lang: item.value for item in blog_header.translations if item.name == "blog_cut"}
        post.blog_text = {item.lang: item.value for item in blog_header.translations if item.name == "blog_text"}

        return post

    @staticmethod
    def populate_from_ui(form):
        post = BlogPost()
        post.name = form.name
        post.url = form.url
        post.visible = form.visible
        post.og_type = form.og_type
        post.og_image = form.og_image

        for field in ["title", "keywords", "description", "og_title", "og_description", "blog_cut", "blog_text"]:
            value = {}
            for lang in cfg.SUPPORTED_LANGS:
                value[lang] = getattr(form, lang+field)

            if len(value) > 0:
                setattr(post, field, value)

    def get_og_title(self, lang):
        return self.og_title[lang]

    def save_to_db(self):
        pass





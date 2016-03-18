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

    def __init__(self, blog_header):
        self.name = blog_header.name
        self.url = blog_header.url
        self.created_at = blog_header.created_at
        self.updated_at = blog_header.updated_at
        self.visible = blog_header.visible
        self.fb_likes = blog_header.fb_likes

        self.title = {item.lang: item for item in blog_header.translations if item.name == "title"}
        self.keywords = {item.lang: item for item in blog_header.translations if item.name == "keywords"}
        self.description = {item.lang: item for item in blog_header.translations if item.name == "description"}

        self.og_type = blog_header.og_type
        self.og_image = blog_header.og_image
        self.og_title = {item.lang: item for item in blog_header.translations if item.name == "og_title"}
        self.og_description = {item.lang: item for item in blog_header.translations if item.name == "og_description"}

    def get_og_title(self, lang):
        return self.og_title[lang]





from flask import render_template, redirect, request

from app.data.blog_posts import BlogPostHeader
from . import front as front_bp
from flask.ext.security import SQLAlchemyUserDatastore
from app import db, User, Role
from app.domain.blog_posts import BlogPost


def get_fb_counters():
    import time
    add = (int(time.time())/3600 - 404750) / 3
    return {"counter1": 14 + add, "counter2": 20 + add}

@front_bp.route("/")
def index():
    return render_template('front/index.html', fb=get_fb_counters())


@front_bp.route("/contact")
def contact():
    return render_template("front/contact.html")



@front_bp.route("/en/baking/chocolate_chips_cookies")
def details_post1():
    return render_template("front/post1.html", fb=get_fb_counters())


@front_bp.route("/en/baking/apple_muffins")
def details_post2():
    return render_template("front/post2.html", fb=get_fb_counters())

@front_bp.route("/test")
def test():
    # todo: get current language
    lang_fallback = ["en"]
    current_lang = "en"
    db_data = BlogPostHeader.query.order_by(BlogPostHeader.created_at).limit(10)
    base_url = "{0}/{1}".format(request.url_root[:request.url_root.find("/", 8)], current_lang)
    posts = [BlogPost.populate_from_db(d, lang_fallback, base_url) for d in db_data]
    return render_template("front/sandbox.html", v={
        "base_url": base_url,
        "posts": posts
    })

@front_bp.route("/data")
def data():
    return "OK"
    db.drop_all()
    db.create_all()
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    from flask_security.utils import encrypt_password
    role = user_datastore.create_role(name="root", description="Site administrator")
    user_datastore.create_user(email='root@site.com', password=encrypt_password('pwd'), roles=[role])
    user_datastore.create_user(email='user@site.com', password=encrypt_password('pwd'))
    db.session.commit()
    return "OK"

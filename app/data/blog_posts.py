from app.core import db
import datetime

class BlogPostHeader(db.Model):
    __tablename__ = 'blog_posts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    url = db.Column(db.String, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime)
    fb_likes = db.Column(db.Integer)
    og_type = db.Column(db.String)
    og_image = db.Column(db.String)

    #todo: tweak lazy value depends on use cases
    translations = db.relationship("Translation", backref="post", lazy="select")


from bin.data import Base
from sqlalchemy import Column, Integer, String, Boolean


class BlogPost(Base):
    __tablename__ = 'blog_posts'

    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True)
    visible = Column(Boolean)
    fb_likes = Column(Integer)


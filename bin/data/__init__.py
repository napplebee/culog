from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from configs import Config as cfg


Engine = create_engine(cfg.SQLALCHEMY_DATABASE_URI)
SessionMaker = sessionmaker(bind=Engine)
db = SessionMaker()
Base = declarative_base()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#TODO IMPLEMENT CORE SETTINGS TO GET ELEMENT TO IMPLEMENT THE URL DB
URL_DATABASE = ''

engine = create_engine(URL_DATABASE)
session = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

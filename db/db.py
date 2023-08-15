from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from ..core.settings import settings

URL_DATABASE = f"mysql+pymsql://{settings.db_user}:{settings.db_root_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

engine = create_engine(URL_DATABASE)
Session_local = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

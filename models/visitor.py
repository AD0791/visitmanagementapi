from ..db import Base
from sqlalchemy import Column, Integer, String, ForeignKey



class Visitor(Base):
    __tablename__ = "visitors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String) 
    phone_number = Column(String)
    company = Column(String)
    visitor_id_number = Column(String, unique=True)

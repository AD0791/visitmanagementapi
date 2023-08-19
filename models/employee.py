from ..db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    department = Column(String)

from ..db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, Date
from sqlalchemy.orm import relationship

class PreRegistration(Base):
    __tablename__ = "preregistrations"

    id = Column(Integer, primary_key=True, index=True)
    expected_date = Column(Date)  

    employee_id = Column(Integer, ForeignKey("employees.id"))
    employee = relationship("Employee")

    visitor_id = Column(Integer, ForeignKey("visitors.id"))
    visitor = relationship("Visitor")

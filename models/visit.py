from ..db import Base
from .visitor import Visitor
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship

class Visit(Base):
    __tablename__ = "visits"

    id = Column(Integer, primary_key=True, index=True)
    purpose = Column(String)
    checkin_time = Column(DateTime)
    checkout_time = Column(DateTime)
    approval_status = Column(Boolean, default=False)

    visitor_id = Column(Integer, ForeignKey("visitors.id"))
    visitor = relationship("Visitor", back_populates="visits")

Visitor.visits = relationship("Visit", order_by=Visit.id, back_populates="visitor")

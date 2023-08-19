from ..db import Base
from .visitor import Visitor
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship

class Badge(Base):
    __tablename__ = "badges"

    id = Column(Integer, primary_key=True, index=True)
    badge_number = Column(String, unique=True)
    printed_status = Column(Boolean, default=False)

    visitor_id = Column(Integer, ForeignKey("visitors.id"))
    visitor = relationship("Visitor", back_populates="badges")

Visitor.badges = relationship("Badge", order_by=Badge.id, back_populates="visitor")

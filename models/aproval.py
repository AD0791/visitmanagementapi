from ..db import Base
from .visit import Visit
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship


class Approval(Base):
    __tablename__ = "approvals"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(Boolean)

    visit_id = Column(Integer, ForeignKey("visits.id"))
    visit = relationship("Visit", back_populates="approvals")

    employee_id = Column(Integer, ForeignKey("employees.id"))
    employee = relationship("Employee")

Visit.approvals = relationship("Approval", order_by=Approval.id, back_populates="visit")
# 

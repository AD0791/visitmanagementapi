from pydantic import BaseModel
from datetime import datetime

class VisitBase(BaseModel):
    purpose: str
    checkin_time: datetime
    checkout_time: datetime

class VisitCreate(VisitBase):
    pass

class Visit(VisitBase):
    id: int
    approval_status: bool

class VisitUpdate(BaseModel):
    approval_status: bool

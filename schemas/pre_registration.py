from pydantic import BaseModel
from datetime import date

class PreRegistrationBase(BaseModel):
    expected_date: date

class PreRegistrationCreate(PreRegistrationBase):
    pass

class PreRegistration(PreRegistrationBase):
    id: int
    employee_id: int
    visitor_id: int

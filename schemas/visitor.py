from pydantic import BaseModel


class VisitorBase(BaseModel):
    name: str
    email: str 
    phone_number: str
    company: str

class VisitorCreate(VisitorBase):
    pass

class Visitor(VisitorBase):
    id: int
    visitor_id_number: str

    class Config:
        orm_mode = True

from pydantic import BaseModel

class BadgeBase(BaseModel):
    badge_number: str
    printed_status: bool

class BadgeCreate(BadgeBase):
    pass

class Badge(BadgeBase):
    id: int
    visitor_id: int

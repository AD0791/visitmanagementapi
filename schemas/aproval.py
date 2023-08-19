from pydantic import BaseModel

class ApprovalBase(BaseModel):
    status: bool

class ApprovalCreate(ApprovalBase):
    pass

class Approval(ApprovalBase):
    id: int
    visit_id: int
    employee_id: int

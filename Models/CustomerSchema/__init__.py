from pydantic import BaseModel, constr, conint
from typing import Optional, List

class CustomerSchema(BaseModel):
    name: str
    dob: constr(min_length=10, max_length=10)
    city: str
    pincode: int
    phone_number: conint(gt=999999999, lt=9999999999)
    email: str
    aadhar_number: conint(gt=99999999999, lt=999999999999)
    accounts: Optional[List[str]] = []
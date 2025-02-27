from pydantic import BaseModel, constr, conint, ConfigDict
from Models.Enums import AccountTypeEnum, AccountStatusEnum

class CurrentAccountSchema(BaseModel):
    account_number: int
    customer_id: int
    customer_phone_number: conint(gt=999999999, lt=9999999999)
    account_type: AccountTypeEnum
    balance: float
    date_opened: str
    status: AccountStatusEnum
    overdraft_limit: int = 5000
    monthly_fee: float = 50.0

    model_config = ConfigDict(arbitrary_types_allowed=True)
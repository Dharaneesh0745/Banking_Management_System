from pydantic import BaseModel, conint, constr, ConfigDict
from Models.Enums import AccountTypeEnum, AccountStatusEnum

class SavingsAccountSchema(BaseModel):
    account_number: int
    customer_id: int
    customer_phone_number: conint(gt=999999999, lt=9999999999)
    account_type: AccountTypeEnum
    date_opened: str
    status: AccountStatusEnum
    balance: float = 500.0
    interest_rate: float = 1.5
    minimum_balance: float = 500.0

    model_config = ConfigDict(arbitrary_types_allowed=True)
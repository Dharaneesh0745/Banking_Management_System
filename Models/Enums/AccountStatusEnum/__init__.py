from enum import Enum

class AccountTypeEnum(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
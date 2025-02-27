from enum import Enum

class AccountType(str, Enum):
    SAVINGS = "Savings"
    CURRENT = "Current"
    
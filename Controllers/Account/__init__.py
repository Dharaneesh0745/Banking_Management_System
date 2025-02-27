from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self, account_number: int, customer_id: int, customer_phone_number: int, account_type: str, balance: float, date_opened: str, status: str):

        self.account_number = account_number
        self.customer_id = customer_id
        self.customer_phone_number = customer_phone_number
        self.account_type = account_type
        self.balance = balance
        self.date_opened = date_opened
        self.status = status

    @abstractmethod
    def get_balance(self) -> float:
        pass

    @abstractmethod
    def get_account_number(self) -> int:
        pass

    @abstractmethod
    def deposit(self, amount) -> bool:
        pass

    @abstractmethod
    def withdraw(self, amount) -> bool:
        pass
from typing_extensions import override

from Controllers.Account import Account
from Models.CurrentAccountSchema import CurrentAccountSchema

class CurrentAccount(Account):

    def __init__(self, current_account_data: CurrentAccountSchema):

        super().__init__(current_account_data.account_number, current_account_data.customer_id, current_account_data.customer_phone_number, current_account_data.account_type, current_account_data.balance, current_account_data.date_opened, current_account_data.status)

        self.overdraft_limit = current_account_data.overdraft_limit
        self.monthly_fee = current_account_data.monthly_fee

    @override
    def get_balance(self) -> float:
        return self.balance

    @override
    def get_account_number(self) -> int:
        return self.account_number

    @override
    def deposit(self, amount) -> bool:
        if amount > 0:
            self.balance += amount
            return True
        return False

    @override
    def withdraw(self, amount: float) -> bool:
        if amount > 0 and (self.balance - amount) >= -self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
            return True
        else:
            print("Withdrawal failed: Exceeds overdraft limit.")
            return False

    def apply_fees(self) -> None:
        self.balance -= self.monthly_fee
        print(f"Applied monthly fee of {self.monthly_fee}. New balance: {self.balance}")

    def __str__(self):
        return f"Current Account => [Account Number: {self.account_number}, Customer Id: {self.customer_id}, Customer Phone Number: {self.customer_phone_number}, Account Type: {self.account_type}, Available Balance: {self.balance}, Date Opened: {self.date_opened}, Status: {self.status}, Overdraft Limit: {self.overdraft_limit}, Monthly Fee: {self.monthly_fee}]"
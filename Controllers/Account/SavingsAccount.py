from typing_extensions import override

from Controllers.Account import Account
from Models.SavingsAccountSchema import SavingsAccountSchema

class SavingsAccount(Account):

    def __init__(self, savings_account_data: SavingsAccountSchema):

        super().__init__(savings_account_data.account_number, savings_account_data.customer_id, savings_account_data.customer_phone_number, savings_account_data.account_type, savings_account_data.balance, savings_account_data.date_opened, savings_account_data.status)

        self.interest_rate = savings_account_data.interest_rate
        self.minimum_balance = savings_account_data.minimum_balance

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
    def withdraw(self, amount) -> bool:
        if self.balance - amount >= self.minimum_balance:
            self.balance -= amount
            return True
        return False

    def calculate_interest(self) -> float:
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest: {interest}. New balance: {self.balance}")
        return interest

    def apply_fees(self) -> None:
        if self.balance < self.minimum_balance:
            fee = 10.0
            self.balance -= fee
            print(f"Applied fee of {fee} for balance below minimum. New balance: {self.balance}")
        else:
            print("No fees applied.")

    def __str__(self):
        return f"Savings Account => [Account Number: {self.account_number}, Customer Id: {self.customer_id}, Customer Phone Number: {self.customer_phone_number}, Account Type: {self.account_type}, Available Balance: {self.balance}, Date Opened: {self.date_opened}, Status: {self.status}, Interest Rate: {self.interest_rate}, Minimum Balance: {self.minimum_balance}]"
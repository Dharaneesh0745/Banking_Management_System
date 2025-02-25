from Account import Account

class CurrentAccount(Account):

    def __init__(self, account_number: int, customer_id: int, customer_phone_number: int, account_type: str, balance: float, date_opened: str, status: str, overdraft_limit: float):

        super().__init__(account_number, customer_id, customer_phone_number,account_type, balance, date_opened, status)

        self.overdraft_limit = overdraft_limit
        self.monthly_fee = 5.0

    def get_balance(self) -> float:
        return self.balance

    def get_account_number(self) -> int:
        return self.account_number

    def deposit(self, amount) -> bool:
        if amount > 0:
            self.balance += amount
            return True
        return False

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
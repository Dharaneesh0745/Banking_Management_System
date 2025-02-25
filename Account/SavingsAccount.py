from Account import Account

class SavingsAccount(Account):

    def __init__(self, account_number: int, customer_id: int, customer_phone_number: int, account_type: str, balance: float, date_opened: str, status: str, interest_rate: float):

        super().__init__(account_number, customer_id, customer_phone_number,account_type, balance, date_opened, status)

        self.interest_rate = interest_rate
        self.minimum_balance = 500

    def get_balance(self) -> float:
        return self.balance

    def get_account_number(self) -> int:
        return self.account_number

    def deposit(self, amount) -> bool:
        if amount > 0:
            self.balance += amount
            return True
        return False

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
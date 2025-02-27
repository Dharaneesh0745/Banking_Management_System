from Services.BankService import BankService
from Models.SavingsAccountSchema import SavingsAccountSchema
from Controllers.Account.SavingsAccount import SavingsAccount
import random
from datetime import date

class ManagerService(BankService):

    @staticmethod
    def create_account(customer_service, phone_number, account_type):
        customer_data, isFound = customer_service.get_particular_customer(phone_number)
        if isFound:
            account_data = {
                "account_number": random.randint(1000000, 10000000),
                "customer_id": customer_data.customer_id,
                "customer_phone_number": phone_number,
                "account_type": account_type,
                "date_opened": str(date.today()),
                "status": "Active"
            }

            if account_type == "Savings":
                account_schema = SavingsAccountSchema(**account_data)
                account = SavingsAccount(account_schema)
                customer_service.add_account_to_collection(account_data, account)
                customer_service.add_account_to_customer_collection(phone_number, account)
                return account, True
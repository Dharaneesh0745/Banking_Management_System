from Models.CustomerSchema import CustomerSchema
from Services.BankService import BankService
from Controllers.Customer import Customer
from Views.CustomerView.CustomerDisplay import CustomerDisplay

class CustomerService(BankService):

    def create_customer(self, customer_data):
        customer_schema = CustomerSchema(**customer_data)
        customer = Customer(customer_schema)
        self._add_customer_to_collection(customer_data, customer)
        return customer

    def get_particular_customer(self, phone_number):
        customer, isFound = self._get_customers(phone_number)
        if isFound:
            return customer, isFound
        CustomerDisplay.customer_not_found()
        return None, False

    def get_all_customers(self):
        return self._get_customers(None)

    def add_account_to_collection(self, account_data, account):
        self._add_account_to_collection(account_data, account)

    def add_account_to_customer_collection(self, phone_number, account):
        self._add_account_to_customer_collection(phone_number, account)

    def get_customer_accounts(self, phone_number):
        account, isFound = self._get_customer_account(phone_number)
        if isFound:
            return account, isFound
        CustomerDisplay.account_not_found()
        return None, False
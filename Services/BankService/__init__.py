from collections import defaultdict
from abc import ABC

class BankService(ABC):

    def __init__(self):
        self.__customers = {}
        self.__accounts = defaultdict(list)

    def _add_customer_to_collection(self, customer_data, customer):
        self.__customers[customer_data["phone_number"]] = customer

    def _get_customers(self, phone_number):
        if phone_number:
            if phone_number in self.__customers:
                return self.__customers[phone_number], True
            return None, False
        return self.__customers

    def _add_account_to_collection(self, account_data, account):
        self.__accounts[account_data["customer_phone_number"]].append(account)

    def _add_account_to_customer_collection(self, phone_number, account):
        self.__customers[phone_number].accounts.append(account)

    def _get_customer_account(self, phone_number):
        if phone_number:
            if phone_number in self.__accounts:
                return self.__accounts[phone_number], True
            return None, False

# from Controllers.Account.SavingsAccount import SavingsAccount
# from Controllers.Account.CurrentAccount import CurrentAccount
# from Controllers.CustomerView import CustomerView
# import random
# from datetime import date
# from collections import defaultdict
# from Models.CustomerSchema import CustomerSchema
# from Models.SavingsAccountSchema import SavingsAccountSchema
# from Models.CurrentAccountSchema import CurrentAccountSchema
#
# if __name__ == "__main__":
#     customers = {}
#     accounts = defaultdict(list)
#
#     print("*** Select a operation ***\n")
#     while True:
#         print()
#         print("1. Create new customer")
#         print("2. View single customer")
#         print("3. View all customers")
#         print("4. Update single customer")
#         print("5. Create new account")
#         print("6. View account")
#         print("7. Deposit amount")
#         print("0. Exit")
#         print()
#
#         operation = int(input("Enter the operation: "))
#
#         match operation:
#             case 1:
#                 # customer_data = {
#                 #     "name": input("Enter name: "),
#                 #     "dob": input("Enter DOB [YYYY-MM-DD]: "),
#                 #     "city": input("Enter city: "),
#                 #     "pincode": int(input("Enter pincode: ")),
#                 #     "phone_number": input("Enter phone number (10 digits): "),
#                 #     "email": input("Enter email: "),
#                 #     "aadhar_number": input("Enter Aadhar number (12 digits): ")
#                 # }
#                 customer_data = {
#                     "name": "Dharaneesh",
#                     "dob": "2005-04-07",
#                     "city": "Coimbatore",
#                     "pincode": "641016",
#                     "phone_number": "9159883009",
#                     "email": "dharaneesh0745@gmail.com",
#                     "aadhar_number": 987654321000
#                 }
#                 customer_schema = CustomerSchema(**customer_data)
#                 customer = CustomerView(customer_schema)
#
#                 customers[customer_data["phone_number"]] = customer
#                 print("CustomerView created successfully!")
#
#             case 2:
#                 phone_number = input("Enter phone number: ")
#                 print(customers[phone_number])
#
#             case 3:
#                 for key, customer in customers.items():
#                     print(customer)
#
#             case 4:
#                 pass
#
#             case 5:
#                 phone_number = input("Enter your phone number: ")
#                 if phone_number not in customers:
#                     print("First register as customer and then create account!!!")
#                     continue
#
#                 account_type = int(input("Enter account type [1 - Savings Account | 2 - Current Account]: "))
#                 customer = customers[phone_number]
#                 account = None
#
#                 if account_type == 1:
#
#                     account_data = {
#                         "account_number": random.randint(100000, 999999),
#                         "customer_id": customers[phone_number].customer_id,
#                         "customer_phone_number": int(phone_number),
#                         "account_type": "Savings",
#                         "balance": float(input("Enter initial balance: ")),
#                         "date_opened": str(date.today()),
#                         "status": "Active"
#                     }
#
#                     account_schema = SavingsAccountSchema(**account_data)
#                     account = SavingsAccount(account_schema)
#
#                 elif account_type == 2:
#
#                     account_data = {
#                         "account_number": random.randint(100000, 999999),
#                         "customer_id": customers[phone_number].customer_id,
#                         "customer_phone_number": int(phone_number),
#                         "account_type": "Current",
#                         "balance": float(input("Enter initial balance: ")),
#                         "date_opened": str(date.today()),
#                         "status": "Active"
#                     }
#
#                     account_schema = CurrentAccountSchema(**account_data)
#                     account = CurrentAccount(account_schema)
#
#                 else:
#                     print("You can able to create only 2 types of Accounts!!!")
#
#                 customer.accounts.append(account)
#                 accounts[phone_number].append(account)
#                 print("Account created successfully!!!")
#
#             case 6:
#                 phone_number = input("Enter phone number: ")
#                 acc = accounts[phone_number]
#                 for account in acc:
#                     print(account)
#
#             case 7:
#                 phone_number = int(input("Enter your phone number: "))
#                 acc = accounts[phone_number]
#                 if not acc:
#                     print("Please create an account to deposit!!!")
#                     continue
#                 for i, account in enumerate(acc):
#                     print(f"{i}. => {account}")
#                 print("\n--- Select your above account to deposit and give the account number ---")
#
#                 account_number = int(input("Enter your account number: "))
#                 deposit = None
#                 for account in acc:
#                     if account.get_account_number() == account_number:
#                         amount = float(input("Enter amount to deposit: "))
#                         deposit = account.deposit(amount)
#                         if deposit:
#                             print("Deposit successful!!!")
#                             print(f"New Balance: {account.get_balance()}")
#                             break
#                 if not deposit:
#                     print("Please enter correct account number!!!")
#
#             case 8:
#                 phone_number = int(input("Enter your phone number: "))
#                 acc = accounts[phone_number]
#                 if not acc:
#                     print("Please create an account to withdraw!!!")
#                     continue
#                 for i, account in enumerate(acc):
#                     print(f"{i}. => {account}")
#                 print("\n--- Select your above account to deposit and give the account number ---")
#
#                 account_number = int(input("Enter your account number: "))
#                 withdraw = None
#                 for account in acc:
#                     if account.get_account_number() == account_number:
#                         withdraw_amount = int(input("Enter withdraw amount: "))
#                         withdraw = account.withdraw(withdraw_amount)
#                         if withdraw:
#                             print("Withdraw successful!!!")
#                             print(f"New Balance: {account.get_balance()}")
#                             break
#                 if not withdraw:
#                     print("Please maintain minimum balance!!!")
#
#             case 0: exit()
#
#             case default:
#                 print("You have entered an invalid operation. Please give the valid one!!!")

from Views.CustomerView import CustomerView
from Views.MainView.MainInput import MainInput
from Views.ManagerView import ManagerView
from Services.CustomerService import CustomerService
from Services.ManagerService import ManagerService
from Views.MainView.MainDisplay import MainDisplay

if __name__ and "__main__":

    customer_service = CustomerService()
    manager_service = ManagerService()

    while True:
        MainDisplay.display_main_options()
        role = MainInput.get_main_options()

        if role == 1:
            customer_view = CustomerView()
            customer_view.main(customer_service)

        elif role == 2:
            manager_view = ManagerView()
            manager_view.main(manager_service, customer_service)

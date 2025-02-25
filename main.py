from Account.SavingsAccount import SavingsAccount
from Account.CurrentAccount import CurrentAccount
from Customer import Customer
import random
from datetime import date
from collections import defaultdict

if __name__ == "__main__":
    customer_id = 1

    customers = {}
    accounts = defaultdict(list)

    print("*** Select a operation ***\n")
    while True:
        print()
        print("1. Create new customer")
        print("2. View single customer")
        print("3. View all customers")
        print("4. Update single customer")
        print("5. Create new account")
        print("6. View account")
        print("7. Deposit amount")
        print("0. Exit")
        print()

        operation = int(input("Enter the operation: "))

        match operation:
            case 1:
                # name = input("Enter name: ")
                # dob = input("Enter DOB - [YY-MM-DD]: ")
                # city = input("Enter city: ")
                # pincode = int(input("Enter pincode: "))
                # phone_number = int(input("Enter phone number: "))
                # email = input("Enter email: ")
                # aadhar_number = int(input("Enter aadhar number: "))

                name = "Dharaneesh"
                dob = "2005-04-07"
                city = "Coimbatore"
                pincode = 641016
                phone_number = 9159883009
                email = "dharaneesh0745@gmail.com"
                aadhar_number = 9876543210

                customer = Customer(customer_id, name, dob, city, pincode, phone_number, email, aadhar_number)

                customers[phone_number] = customer
                print("Customer created successfully!")
                customer_id += 1

            case 2:
                phone_number = int(input("Enter phone number: "))
                print(customers[phone_number])

            case 3:
                for key, customer in customers.items():
                    print(customer)

            case 4:
                pass

            case 5:
                phone_number = int(input("Enter your phone number: "))
                if phone_number not in customers:
                    print("First register as customer and then create account!!!")
                    continue

                account_type = int(input("Enter account type [1 - Savings Account | 2 - Current Account]: "))
                initial_balance = float(input("Enter initial balance: "))
                customer = customers[phone_number]
                account_number = random.randint(100000, 999999)
                today_date = str(date.today())
                account = None

                if account_type == 1:
                    account = SavingsAccount(account_number, customer.customer_id, customer.phone_number, "Savings",
                                             initial_balance, today_date, "Active", 1.5)

                elif account_type == 2:
                    account = CurrentAccount(account_number, customer.customer_id, customer.phone_number, "Current",
                                             initial_balance, today_date, "Active", 5000)

                else:
                    print("You can able to create only 2 types of Accounts!!!")

                customer.accounts.append(account)
                accounts[phone_number].append(account)
                print("Account created successfully!!!")

            case 6:
                phone_number = int(input("Enter phone number: "))
                acc = accounts[phone_number]
                for account in acc:
                    print(account)

            case 7:
                phone_number = int(input("Enter your phone number: "))
                acc = accounts[phone_number]
                if not acc:
                    print("Please create an account to deposit!!!")
                    continue
                for i, account in enumerate(acc):
                    print(f"{i}. => {account}")
                print("\n--- Select your above account to deposit and give the account number ---")

                account_number = int(input("Enter your account number: "))
                deposit = None
                for account in acc:
                    if account.get_account_number() == account_number:
                        amount = float(input("Enter amount to deposit: "))
                        deposit = account.deposit(amount)
                        if deposit:
                            print("Deposit successful!!!")
                            print(f"New Balance: {account.get_balance()}")
                            break
                if not deposit:
                    print("Please enter correct account number!!!")

            case 8:
                phone_number = int(input("Enter your phone number: "))
                acc = accounts[phone_number]
                if not acc:
                    print("Please create an account to withdraw!!!")
                    continue
                for i, account in enumerate(acc):
                    print(f"{i}. => {account}")
                print("\n--- Select your above account to deposit and give the account number ---")

                account_number = int(input("Enter your account number: "))
                withdraw = None
                for account in acc:
                    if account.get_account_number() == account_number:
                        withdraw_amount = int(input("Enter withdraw amount: "))
                        withdraw = account.withdraw(withdraw_amount)
                        if withdraw:
                            print("Withdraw successful!!!")
                            print(f"New Balance: {account.get_balance()}")
                            break
                if not withdraw:
                    print("Please maintain minimum balance!!!")

            case 0: exit()

            case default:
                print("You have entered an invalid operation. Please give the valid one!!!")

class CustomerDisplay:

    @staticmethod
    def display_operations():
        print("\n*** Select an operation ***")
        print("1. Create new customer")
        print("2. View your full details")
        print("3. View accounts details")
        print("4. Deposit amount")
        print("5. Withdraw amount")
        print("0. Exit")

    @staticmethod
    def customer_created(customer):
        print("Customer Created Successfully!!!")
        print("Newly Created: ", customer)

    @staticmethod
    def display_customer(customer):
        print("Your Details: ", customer)

    @staticmethod
    def customer_not_found():
        print("Customer Not Found!!! Create a new customer first...")

    @staticmethod
    def display_account_types():
        print("\n1. Savings Account [1]")
        print("2. Current Account [2]")

    @staticmethod
    def account_created(account):
        print("Account Created Successfully!!!")
        print("Newly Created: ", account)

    @staticmethod
    def account_not_found():
        print("No Accounts Found, Ask bank manager to create account!!!")

    @staticmethod
    def display_accounts(accounts):
        for account in accounts:
            print(account)
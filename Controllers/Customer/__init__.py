from Models.CustomerSchema import CustomerSchema

class Customer:
    __id_counter = 1

    def __init__(self, customer_data: CustomerSchema):

        global accounts

        if not customer_data.accounts:
            accounts = []
        self.customer_id = self.__id_counter
        self.name = customer_data.name
        self.dob = customer_data.dob
        self.city = customer_data.city
        self.pincode = customer_data.pincode
        self.phone_number = customer_data.phone_number
        self.email = customer_data.email
        self.aadhar_number = customer_data.aadhar_number
        self.accounts = accounts

        self.__id_counter += 1

    def __str__(self) -> str:
        return f"Customer [Id: {self.customer_id}, Name: {self.name}, DOB: {self.dob}, City: {self.city}, Pincode: {self.pincode}, Phone Number: {self.phone_number}, Email: {self.email}, Aadhar Number: {self.aadhar_number}, Associated Accounts: {[str(account) for account in self.accounts]}]"

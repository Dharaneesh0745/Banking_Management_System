class Customer:

    def __init__(self, customer_id: int, name: str, dob: str, city: str, pincode: int, phone_number: int, email: str, aadhar_number: int,
                 accounts=None):

        if accounts is None:
            accounts = []
        self.customer_id = customer_id
        self.name = name
        self.dob = dob
        self.city = city
        self.pincode = pincode
        self.phone_number = phone_number
        self.email = email
        self.aadhar_number = aadhar_number
        self.accounts = accounts

    def __str__(self) -> str:
        return f"Customer [Id: {self.customer_id}, Name: {self.name}, DOB: {self.dob}, City: {self.city}, Pincode: {self.pincode}, Phone Number: {self.phone_number}, Email: {self.email}, Aadhar Number: {self.aadhar_number}, Associated Accounts: {[str(account) for account in self.accounts]}]"

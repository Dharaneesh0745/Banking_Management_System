from Views.CustomerView.CustomerInput import CustomerInput
from Services.CustomerService import CustomerService
from Views.CustomerView.CustomerDisplay import CustomerDisplay

class CustomerView:

    @staticmethod
    def main(customer_service):

        while True:
            CustomerDisplay.display_operations()

            operation = CustomerInput.get_customer_operation()

            match operation:
                case 1:
                    customer_data = CustomerInput.get_customer_input()
                    customer = customer_service.create_customer(customer_data)
                    CustomerDisplay.customer_created(customer)

                case 2:
                    phone_number = CustomerInput.get_customer_phone_number()
                    customer, isFound = customer_service.get_particular_customer(phone_number)
                    CustomerDisplay.display_customer(customer)

                case 3:
                    phone_number = CustomerInput.get_customer_phone_number()
                    accounts, isFound = customer_service.get_customer_accounts(phone_number)
                    if isFound:
                        CustomerDisplay.display_accounts(accounts)

            return
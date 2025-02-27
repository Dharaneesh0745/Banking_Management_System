from Views.CustomerView.CustomerInput import CustomerInput
from Views.ManagerView.ManagerDisplay import ManagerDisplay
from Views.ManagerView.ManagerInput import ManagerInput
from Views.CustomerView.CustomerDisplay import CustomerDisplay
from Services.ManagerService import ManagerService

class ManagerView:

    @staticmethod
    def main(manager_service, customer_service):

        while True:
            ManagerDisplay.display_operations()

            operation = ManagerInput.get_manager_operation()

            match operation:
                case 1:
                    customer_phone_number = CustomerInput.get_customer_phone_number()
                    CustomerDisplay.display_account_types()
                    account_type = CustomerInput.get_account_type()
                    account = None
                    isCreated = False
                    if account_type == 1:
                        account, isCreated = manager_service.create_account(customer_service, customer_phone_number, "Savings")
                    if isCreated:
                        CustomerDisplay.account_created(account)

            return
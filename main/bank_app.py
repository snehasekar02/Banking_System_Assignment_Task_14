from entity.customer import Customer
from dao.bank_repository_impl import BankRepositoryImpl
from exception import exception


class BankApp:
    def __init__(self):
        self.bank_service = BankRepositoryImpl()

    def main(self):
        try:
            print("Welcome to the Banking System!")
            while True:
                print("\nMenu:")
                print("1. Create Account")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Get Balance")
                print("5. Transfer")
                print("6. Get Account Details")
                print("7. List Accounts")
                print("8. Get Transactions")
                print("9. Exit")

                choice = input("Enter your choice: ")

                if choice == '1':
                    self.create_account_menu()
                elif choice == '2':
                    self.deposit()
                elif choice == '3':
                    self.withdraw()
                elif choice == '4':
                    self.get_balance()
                elif choice == '5':
                    self.transfer()
                elif choice == '6':
                    self.get_account_details()
                elif choice == '7':
                    self.list_accounts()
                elif choice == '8':
                    self.get_transactions()
                elif choice == '9':
                    print("Thank you for using the Banking System!")
                    break
                else:
                    print("Invalid choice. Please try again.")
        except exception.NullPointerException as e:
            print("Error:", e)

    def create_account_menu(self):
        print("\nCreate Account:")
        print("1. Savings Account")
        print("2. Current Account")
        print("3. Zero Balance Account")

        choice = input("Enter your choice: ")

        if choice == '1':
            self.create_account("savings")
        elif choice == '2':
            self.create_account("current")
        elif choice == '3':
            self.create_account("zero_balance")
        else:
            print("Invalid choice. Please try again.")

    def create_account(self, acc_type):
        customer_id = int(input("Enter customer id: "))
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        dob = input("Enter DOB: ")
        email = input("Enter email address: ")
        phone_number = input("Enter phone number: ")
        address = input("Enter address: ")

        customer = Customer(customer_id, first_name, last_name, dob, email, phone_number, address)
        initial_balance = float(input("Enter initial balance: "))

        try:
            self.bank_service.createAccount(customer, acc_type, initial_balance)
            print("Account created successfully!")
        except exception.InvalidAccountTypeException as e:
            print("Error:", e)
        except exception.SQLException as e:
            print("Database error:", e)

    def deposit(self):
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter amount to deposit: "))

        try:
            new_balance = self.bank_service.deposit(account_number, amount)
            if new_balance is not None:
                print(f"Rs.{amount} deposited successfully. New balance: Rs.{new_balance}")
        except ValueError as e:
            print("Error:", e)

    def withdraw(self):
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter amount to withdraw: "))

        try:
            new_balance = self.bank_service.withdraw(account_number, amount)
            if new_balance is not None:
                print(f"Rs.{amount} withdrawn successfully. New balance: Rs.{new_balance}")
        except ValueError as e:
            print("Error:", e)

    def get_balance(self):
        account_number = int(input("Enter account number: "))

        try:
            balance = self.bank_service.getAccountBalance(account_number)
            if balance is not None:
                print(f"Account balance: Rs.{balance}")
        except ValueError as e:
            print("Error:", e)

    def transfer(self):
        from_account_number = int(input("Enter sender account number: "))
        to_account_number = int(input("Enter receiver account number: "))
        amount = float(input("Enter amount to transfer: "))

        try:
            success = self.bank_service.transfer(from_account_number, to_account_number, amount)
            if success:
                print(f"Rs.{amount} transferred successfully.")
            else:
                print("Transfer failed.")
        except ValueError as e:
            print("Error:", e)

    def get_account_details(self):
        account_number = int(input("Enter account number: "))

        try:
            account = self.bank_service.getAccountDetails(account_number)
            if account is not None:
                print(account)
        except ValueError as e:
            print("Error:", e)

    def list_accounts(self):
        accounts = self.bank_service.listAccounts()
        print("\nList of Accounts:")
        for account in accounts:
            print(account)

    def get_transactions(self):
        account_number = int(input("Enter account number: "))
        from_date = input("Enter start date (YYYY-MM-DD): ")
        to_date = input("Enter end date (YYYY-MM-DD): ")

        try:
            transactions = self.bank_service.getTransactions(account_number, from_date, to_date)
            if transactions:
                print("\nTransactions:")
                for transaction in transactions:
                    print(transaction)
            else:
                print("No transactions found.")
        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    bank_app = BankApp()
    bank_app.main()

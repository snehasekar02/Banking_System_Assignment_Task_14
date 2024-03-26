from entity.customer import Customer


class Account:
    last_acc_no = 1000

    def __init__(self, account_type: str, balance: float, customer: Customer):
        Account.last_acc_no += 1
        self.account_number = Account.last_acc_no
        self.account_type = account_type
        self.balance = balance
        self.customer = customer

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_account_type(self):
        return self.account_type

    def set_account_type(self, account_type):
        self.account_type = account_type

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def get_customer(self):
        return self.customer

    def set_customer(self, customer):
        self.customer = customer

    def __str__(self):
        return f"Account Number: {self.account_number}, Type: {self.account_type}, Balance: {self.balance}, Customer: {self.customer}"

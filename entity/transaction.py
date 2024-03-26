from entity.account import Account


class Transaction:
    def __init__(self, account: Account, description: str, transaction_type: str, transaction_amount: float, date: str):
        self.account = account
        self.description = description
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount
        self.date_time = date

    def get_account(self):
        return self.account

    def set_account(self, account):
        self.account = account

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_transaction_type(self):
        return self.transaction_type

    def set_transaction_type(self, transaction_type):
        self.transaction_type = transaction_type

    def get_transaction_amount(self):
        return self.transaction_amount

    def set_transaction_amount(self, transaction_amount):
        self.transaction_amount = transaction_amount

    def get_date_time(self):
        return self.date_time

    def set_date_time(self, date_time):
        self.date_time = date_time

    def __str__(self):
        return f"Transaction: {self.transaction_type}, Amount: {self.transaction_amount}, Description: {self.description}, Date: {self.date_time}"

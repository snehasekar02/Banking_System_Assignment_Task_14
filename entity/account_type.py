from entity.account import Account
from entity.customer import Customer


class SavingsAccount(Account):
    interest_rate = None

    def __init__(self, balance: float, customer: Customer, interest_rate: float):
        super().__init__("savings", balance, customer)
        if balance < 500:
            raise ValueError("Minimum balance for a savings account is 500")
        self.interest_rate = interest_rate

    def get_interest_rate(self):
        return self.interest_rate

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def __str__(self):
        return f"Savings Account - Account Number: {self.account_number}, Balance: {self.balance}, Customer: {self.customer}, Interest Rate: {self.interest_rate}"


class CurrentAccount(Account):
    def __init__(self, balance: float, customer: Customer, overdraft_limit: float):
        super().__init__("current", balance, customer)
        self.overdraft_limit = overdraft_limit

    def get_overdraft_limit(self):
        return self.overdraft_limit

    def set_overdraft_limit(self, overdraft_limit):
        self.overdraft_limit = overdraft_limit

    def __str__(self):
        return f"Current Account - Account Number: {self.account_number}, Balance: {self.balance}, Customer: {self.customer}, Overdraft Limit: {self.overdraft_limit}"


class ZeroBalanceAccount(Account):
    def __init__(self, customer: Customer):
        super().__init__("zero balance", 0, customer)

    def __str__(self):
        return f"Zero Balance Account - Account Number: {self.account_number}, Balance: {self.balance}, Customer: {self.customer}"

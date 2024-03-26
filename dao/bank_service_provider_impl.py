from abc import ABC
from typing import List
from entity.account import Account
from entity.account_type import SavingsAccount, CurrentAccount, ZeroBalanceAccount
from entity.customer import Customer
from entity.transaction import Transaction
from dao.customer_service_provider_impl import CustomerServiceProviderImpl
from dao.ibank_service_provider import IBankServiceProvider


class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider, ABC):
    def __init__(self, branchName: str, branchAddress: str):
        super().__init__()
        self.accountList: List[Account] = []
        self.transactionList: List[Transaction] = []
        self.branchName = branchName
        self.branchAddress = branchAddress

    def create_account(self, customer: Customer, accNo: int, accType: str, balance: float) -> Account:
        if accType == "Savings":
            if balance < 500:
                raise ValueError("Minimum balance for a savings account is 500.")
            new_account = SavingsAccount(balance, customer, 4.50)
        elif accType == "Current":
            new_account = CurrentAccount(balance, customer, 1000)
        elif accType == "ZeroBalance":
            new_account = ZeroBalanceAccount(customer)
        else:
            raise ValueError("Invalid account type.")

        self.accountList.append(new_account)
        return new_account

    def listAccounts(self) -> List:
        return self.accountList

    def getAccountDetails(self, account_number) -> Account | None:
        for account in self.accountList:
            if account.get_account_number() == account_number:
                return account
        return None

    def calculateInterest(self):
        for account in self.accountList:
            if isinstance(account, SavingsAccount):
                interest = account.get_balance() * (account.get_interest_rate() / 100)
                account.set_balance(account.get_balance() + interest)

    '''def deposit(self, account_number, amount):
        # Implement deposit functionality
        pass

    def withdraw(self, account_number, amount):
        # Implement withdraw functionality
        pass

    def transfer(self, from_account_number, to_account_number, amount):
        # Implement transfer functionality
        pass

    def get_transactions(self, account_number, from_date, to_date):
        # Implement logic to retrieve transactions between specified dates
        pass'''



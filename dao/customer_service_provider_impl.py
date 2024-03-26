from typing import List, Any
from dao.ibank_service_provider import IBankServiceProvider
from dao.icustomer_service_provider import ICustomerServiceProvider
from entity.account_type import SavingsAccount, CurrentAccount
from entity.transaction import Transaction


class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self, bank: IBankServiceProvider):
        self.bank = bank

    def get_account_balance(self, account_number: int) -> float | None:
        account = self.bank.get_account_details(account_number)
        if account:
            return account.balance
        else:
            return None

    def deposit(self, account_number: int, amount: float) -> float | None:
        account = self.bank.get_account_details(account_number)
        if account:
            account.balance += amount
            print(f"Rs.{amount} deposited!!")
            print(f"New balance is {account.balance}")
            return account.balance
        else:
            return None

    def withdraw(self, account_number: int, amount: float) -> float:
        account = self.bank.get_account_details(account_number)
        if account:
            if isinstance(account, SavingsAccount) and account.balance - amount < 500:
                print("Withdrawal violates minimum balance rule for Savings Account.")
                return account.balance
            elif isinstance(account, CurrentAccount) and amount > account.balance + account.overdraft_limit:
                print("Withdrawal amount exceeds available balance and overdraft limit for Current Account.")
                return account.balance
            else:
                account.balance -= amount
                print(f"Rs.{amount} withdrawn!!")
                print(f"New balance is {account.balance}")
                return account.balance
        else:
            return 0.0

    def transfer(self, from_account_number: int, to_account_number: int, amount: float) -> bool:
        from_account = self.bank.get_account_details(from_account_number)
        to_account = self.bank.get_account_details(to_account_number)
        if from_account and to_account:
            if isinstance(from_account, SavingsAccount) and from_account.balance - amount < 500:
                print("Transfer violates minimum balance rule for Savings Account.")
                return False
            elif isinstance(from_account,
                            CurrentAccount) and amount > from_account.balance + from_account.overdraft_limit:
                print("Transfer amount exceeds available balance and overdraft limit for Current Account.")
                return False
            else:
                from_account.balance -= amount
                to_account.balance += amount
                return True
        else:
            return False

    def get_account_details(self, account_number: int):
        return self.bank.get_account_details(account_number)

    def get_transactions(self, account_number: int, from_date: str, to_date: str) -> List[Transaction]:
        transactions = []

        account = self.bank.get_account_details(account_number)
        if account:
            all_transactions = account.transactions

            for transaction in all_transactions:
                if from_date <= transaction.date <= to_date:
                    transactions.append(transaction)

        return transactions

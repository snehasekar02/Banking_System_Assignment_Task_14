from abc import ABC, abstractmethod
from typing import List
from entity.account import Account
from entity.customer import Customer


class IBankRepository(ABC):
    @abstractmethod
    def createAccount(self, customer: Customer, accType: str, balance: float) -> None:
        pass

    @abstractmethod
    def listAccounts(self) -> List[Account]:
        pass

    @abstractmethod
    def calculateInterest(self) -> None:
        pass

    @abstractmethod
    def getAccountBalance(self, account_number: int) -> float:
        pass

    @abstractmethod
    def deposit(self, account_number: int, amount: float) -> float:
        pass

    @abstractmethod
    def withdraw(self, account_number: int, amount: float) -> float:
        pass

    @abstractmethod
    def transfer(self, from_account_number: int, to_account_number: int, amount: float) -> None:
        pass

    @abstractmethod
    def getAccountDetails(self, account_number: int) -> Account:
        pass

    @abstractmethod
    def getTransactions(self, account_number: int, from_date: str, to_date: str) -> List[str]:
        pass

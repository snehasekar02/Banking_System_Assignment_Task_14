from abc import ABC, abstractmethod
from typing import List


class ICustomerServiceProvider(ABC):
    @abstractmethod
    def get_account_balance(self, account_number: int) -> float:
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
    def get_account_details(self, account_number: int):
        pass

    @abstractmethod
    def get_transactions(self, account_number: int, from_date: str, to_date: str) -> List[str]:
        pass

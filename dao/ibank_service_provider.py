from entity.account import Account
from abc import ABC, abstractmethod
from typing import List


class IBankServiceProvider(ABC):
    @abstractmethod
    def create_account(self, customer, accNo: int, accType: str, balance: float) -> None:
        pass

    @abstractmethod
    def list_accounts(self) -> List[Account]:
        pass

    @abstractmethod
    def get_account_details(self, account_number: int):
        pass

    @abstractmethod
    def calculate_interest(self) -> None:
        pass

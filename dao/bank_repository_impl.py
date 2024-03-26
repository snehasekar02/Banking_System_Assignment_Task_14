from abc import ABC
from typing import List, Union, Any
from exception import exception
from dao.bank_service_provider_impl import BankServiceProviderImpl
from entity import account
from entity.account import Account
from entity.account_type import SavingsAccount
from entity.customer import Customer
from dao.ibank_repository import IBankRepository
from util.db_connection import DBUtil
from dao.ibank_service_provider import IBankServiceProvider
import pymysql.cursors

from entity.transaction import Transaction


class BankRepositoryImpl(IBankRepository, ABC):
    def __init__(self):
        self.connection = DBUtil.getDBConn()

    def createAccount(self, customer: Customer, accType: str, balance: float) -> bool:
        try:
            with self.connection.cursor() as cursor:
                customer_id = customer.customer_id
                first_name = customer.first_name
                last_name = customer.last_name
                dob = customer.dob
                email = customer.email
                phone = customer.phone
                address = customer.address

                sql1 = (
                    "INSERT INTO Customers (customer_id, first_name, last_name, DOB, email, phone_number, address) VALUES "
                    "( %s, %s, %s, %s, %s, %s, %s)")
                sql = "INSERT INTO Accounts (customer_id, account_type, balance) VALUES ( %s, %s, %s)"
                cursor.execute(sql1, (customer_id, first_name, last_name, dob, email, phone, address))
                cursor.execute(sql, (customer.customer_id, accType, balance))
            self.connection.commit()
            return True
        except exception.SQLException as e:
            print("Error creating account:", e)
            return False
        finally:
            self.connection.close()

    def listAccounts(self) -> List[Account]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM Accounts"
                cursor.execute(sql)
                result = cursor.fetchall()

                accounts = []
                for row in result:
                    acc = Account(row['customer_id'], row['account_type'], row['balance'])
                    accounts.append(acc)
                return accounts
        except Exception as e:
            print("Error listing accounts:", e)
            return []

    def calculateInterest(self):
        try:
            with self.connection.cursor() as cursor:
                # Retrieve all accounts
                sql = "SELECT * FROM Accounts"
                cursor.execute(sql)
                accounts = cursor.fetchall()

                for acc in accounts:
                    if acc['account_type'] == 'savings':
                        interest = acc['balance'] * (SavingsAccount.interest_rate / 100)
                        new_balance = acc['balance'] + interest

                        update_sql = "UPDATE Accounts SET balance = %s WHERE account_id = %s"
                        cursor.execute(update_sql, (new_balance, acc['account_id']))

                self.connection.commit()

                print("Interest calculated and updated successfully.")

        except Exception as e:
            print("Error calculating interest:", e)
            self.connection.rollback()

    def getAccountBalance(self, account_number: int) -> float:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT balance FROM Accounts WHERE account_id = %s"
                cursor.execute(sql, (account_number,))
                result = cursor.fetchone()
                if result:
                    return result['balance']
                else:
                    return 0.0
        except Exception as e:
            print("Error getting account balance:", e)
            return 0.0

    def deposit(self, account_number: int, amount: float) -> float:
        try:
            with self.connection.cursor() as cursor:
                current_balance = self.getAccountBalance(account_number)
                new_balance = current_balance + amount
                sql = "UPDATE Accounts SET balance = %s WHERE account_id = %s"
                cursor.execute(sql, (new_balance, account_number))
                self.connection.commit()
                return new_balance
        except Exception as e:
            print("Error depositing amount:", e)
            return -1.0

    def withdraw(self, account_number: int, amount: float) -> float:
        try:
            with self.connection.cursor() as cursor:
                current_balance = self.getAccountBalance(account_number)
                new_balance = current_balance - amount
                print(new_balance)
                sql = "UPDATE Accounts SET balance = %s WHERE account_id = %s"
                cursor.execute(sql, (new_balance, account_number))
                self.connection.commit()
                return new_balance
        except exception.OverDraftLimitExceededException as e:
            print("Error:", e)
            return -1.0
        except exception.InsufficientFundException as e:
            print("Error:", e)
            return -1.0
        except exception.NullPointerException as e:
            print("Error:", e)
            return -1.0
        except Exception as e:
            print("Error withdrawing amount:", e)
            return -1.0

    def transfer(self, from_account_number: int, to_account_number: int, amount: float) -> bool:
        try:
            with self.connection.cursor() as cursor:
                new_balance_sender = self.withdraw(from_account_number, amount)

                new_balance_receiver = self.deposit(to_account_number, amount)

                if new_balance_sender >= 0 and new_balance_receiver >= 0:
                    return True
                else:
                    self.connection.rollback()
                    return False
        except exception.InvalidAccountException as e:
            print("Error:", e)
            return False
        except Exception as e:
            print("Error transferring amount:", e)
            return False

    def getAccountDetails(self, account_number: int) -> Union[Account, None]:
        try:
            with self.connection.cursor() as cursor:
                # Retrieve account details by account number
                sql = "SELECT * FROM Accounts WHERE account_id = %s"
                cursor.execute(sql, (account_number,))
                result = cursor.fetchone()

                if result:
                    acc = Account(result['customer_id'], result['account_type'],
                                  result['balance'])
                    return acc
                else:
                    return None
        except Exception as e:
            print("Error getting account details:", e)
            return None

    def getTransactions(self, account_number: int, from_date: str, to_date: str) -> list[Transaction] | list[Any]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM Transactions WHERE account_id = %s AND transaction_date BETWEEN %s AND %s"
                cursor.execute(sql, (account_number, from_date, to_date))
                result = cursor.fetchall()

                transactions = []
                for row in result:
                    transaction = Transaction(row['transaction_id'], row['account_id'], row['transaction_type'],
                                              row['amount'], row['transaction_date'])
                    transactions.append(transaction)
                return transactions
        except Exception as e:
            print("Error getting transactions:", e)
            return []

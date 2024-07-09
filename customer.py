# Customer Details
import sqlite3
import constant
from database import BankingDatabase
from constant import USER_CREATION_ERROR


class Customer(BankingDatabase):
    """
    class implemented for customer
    """

    def __init__(self, username, password, name, age, address, account_number) -> None:
        super().__init__()
        self.__customer_details = {
            "username": username.lower(),
            "password": password,
            "name": name.lower(),
            "age": age,
            "address": address,
            "account_number": account_number,
        }

    def create_user(self) -> None:
        """
        methods to Execute a user creation query
        @return: None
        """
        print(self.__customer_details)
        try:
            self.cursor.execute(
                "INSERT INTO customers (username, password, name, age, address, account_number) VALUES (:username, "
                ":password, :name, :age, :address, :account_number);", self.__customer_details)
            self.db.commit()
        except sqlite3.ProgrammingError as e:
            print(USER_CREATION_ERROR)
            print(constant.PROGRAMMING_ERROR, e)
            return
        except sqlite3.OperationalError as e:
            print(USER_CREATION_ERROR)
            print(constant.OPERATIONAL_ERROR, e)
            return


if __name__ == "__main__":
    pass
    # obj = Customer("test", "test", "test", "test", "test", "test")
    # obj.create_user()

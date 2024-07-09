"""Database Management Banking"""

import constant
from sqlite3 import connect, OperationalError, ProgrammingError


class BankingDatabase:
    """
    class To Implement Banking Database
    """

    def __init__(self) -> None:
        self.db = connect(constant.DB)
        self.cursor = self.db.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS customers
                (id INTEGER PRIMARY KEY,
                username VARCHAR(20) NOT NULL,
                password VARCHAR(20) NOT NULL,
                name varchar(20) NOT NULL,
                age INTEGER NOT NULL,
                address VARCHAR(64) NOT NULL,
                balance INT NOT NULL DEFAULT 0,
                account_number INT NOT NULL,
                status BOOLEAN NOT NULL DEFAULT 1)"""
        )

    def create_transaction_table(self, username):
        """
        method to create transaction table for username passed in parameter
        @param username: str
        @return: None
        """
        try:
            self.cursor.execute(
                f"""CREATE TABLE IF NOT EXISTS {username}_transaction
                               (id INTEGER PRIMARY KEY,
                               date varchar(32) NOT NULL,
                               credit INT NOT NULL DEFAULT 0,
                               debit INT NOT NULL DEFAULT 0,
                               remaining_balance INT NOT NULL,
                               remark varchar(132) NOT NULL)"""
            )
            self.db.commit()
        except OperationalError as e:
            print(constant.OPERATIONAL_ERROR, e)
            return
        except ProgrammingError as e:
            print(constant.PROGRAMMING_ERROR, e)
            return
        except Exception as e:
            print(constant.UNKNOWN_ERROR, e)


if __name__ == "__main__":
    obj = BankingDatabase()

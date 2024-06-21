"""Database Management Banking"""
import constant
from sqlite3 import connect

class BankingDatabase:
    """
    class To Implement Banking Databae
    """
    def __init__(self):
        self.db = connect(constant.DB)
        self.cursor = self.db.cursor()

    def execute_query(self, query: str, status=True) -> tuple:
        """
        instance Method to Execute Database Query
        @param query: str
        @param status:
        @return: tuple
        """


def db_query(s, status=True):
    cursor.execute(s)
    if status:
        result = cursor.fetchall()
        return result


def createcustomertable():
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers
                (username VARCHAR(20) NOT NULL,
                password VARCHAR(20) NOT NULL,
                name varchar(20) NOT NULL,
                age INTEGER NOT NULL,
                city VARCHAR(20) NOT NULL,
                balance INTEGER NOT NULL,
                account_number INTEGER NOT NULL,
                status BOOLEAN NOT NULL)
    ''')


if __name__ == "__main__":
    createcustomertable()
    mydb.commit()

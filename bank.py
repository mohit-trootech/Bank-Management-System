# Bank Services
import constant
from database import BankingDatabase, OperationalError, ProgrammingError
from utils import custom_print, InsufficientBalanceError, AccountNotExist


class Bank(BankingDatabase):
    def __init__(self, username, account_number):
        super().__init__()
        self.__username = username
        self.__account_number = account_number

    def user_details(self) -> None:
        """
        Bank method to print User Details
        @return: None
        """
        self.cursor.execute(f"SELECT * FROM customers WHERE username = '{self.__username}';")
        custom_print("User Details")
        print(self.cursor.fetchone()[1:-1])

    def balance_enquiry(self) -> None:
        """
        return User Account Balance
        @return: None
        """
        self.cursor.execute(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        print(constant.CUSTOM_FORMAT)
        print("Available Balance {}".format(self.cursor.fetchone()[0]))

    def user_credit(self, amount: int) -> None:
        """
        Bank method to credit and update credit information
        @param amount: int
        @return: None
        """
        try:
            self.cursor.execute(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
            updated_balance = self.cursor.fetchone()[0] + amount
            self.cursor.execute(f"UPDATE customers SET balance = '{updated_balance}' "
                                f"WHERE username = '{self.__username}';")
            self.balance_enquiry()
            self.cursor.execute(f"INSERT INTO {self.__username}_transaction "
                                f"(date, credit, remaining_balance, remark)"
                                f"VALUES ('{constant.CURRENT_TIME}',{amount}, {updated_balance}, "
                                f"'{constant.REMARK_CREDIT.format(amount=amount)}');")
            self.db.commit()
            custom_print(constant.CREDIT_SUCCESS)
        except OperationalError as e:
            print(constant.OPERATIONAL_ERROR, e)
            return
        except ProgrammingError as e:
            print(constant.PROGRAMMING_ERROR, e)
            return

    def user_debit(self, amount: int) -> None:
        try:
            user_balance = self.cursor.execute(f"SELECT balance FROM customers"
                                               f" WHERE username = '{self.__username}';").fetchone()[0]
            if user_balance < amount:
                raise InsufficientBalanceError()
            updated_balance = user_balance - amount
            self.cursor.execute(f"UPDATE customers SET balance = '{updated_balance}' "
                                f"WHERE username = '{self.__username}';")
            self.balance_enquiry()
            self.cursor.execute(f"INSERT INTO {self.__username}_transaction "
                                f"(date, debit, remaining_balance, remark) VALUES "
                                f"('{constant.CURRENT_TIME}',{amount}, {updated_balance}, "
                                f"'{constant.REMARK_DEBIT.format(amount=amount)}');")
            self.db.commit()
            custom_print(constant.DEBIT_SUCCESS)
            return
        except InsufficientBalanceError as ibe:
            print(ibe)
            return
        except OperationalError as e:
            print(constant.OPERATIONAL_ERROR, e)
            return
        except ProgrammingError as e:
            print(constant.PROGRAMMING_ERROR, e)
            return

    def transfer_funds(self, receiver_account, amount) -> None:
        """
        Bank method to transfer Funds into Another Bank Account
        @param receiver_account: int
        @param amount: int
        @return: None
        """
        try:
            user_balance = self.cursor.execute(f"SELECT balance FROM customers "
                                               f"WHERE username = '{self.__username}';").fetchone()[0]
            if user_balance < amount:
                raise InsufficientBalanceError()
            receiver_balance = self.cursor.execute(f"SELECT balance FROM customers "
                                                   f"WHERE account_number = '{receiver_account}';").fetchone()
            if not receiver_balance:
                raise AccountNotExist()
            user_balance = user_balance - amount
            self.cursor.execute(f"UPDATE customers "
                                f"SET balance = '{user_balance}' "
                                f"WHERE username = '{self.__username}'; ")
            receiver_balance = receiver_balance[0] + amount
            receiver_username = self.cursor.execute(f"SELECT username FROM customers "
                                                    f"where account_number = '{receiver_account}';").fetchone()[0]
            self.cursor.execute(f"UPDATE customers "
                                f"SET balance = '{receiver_balance}' "
                                f"WHERE account_number = '{receiver_account}';")
            self.cursor.execute(f"INSERT INTO {self.__username}_transaction "
                                f"(date, debit, remaining_balance, remark) VALUES "
                                f"('{constant.CURRENT_TIME}', {amount},"
                                f"{user_balance},"
                                f" '{constant.REMARK_TRANSFER.format(amount=amount, transfer=receiver_account)}');")
            self.cursor.execute(f"INSERT INTO {receiver_username}_transaction "
                                f"(date, credit, remaining_balance, remark) VALUES "
                                f"('{constant.CURRENT_TIME}', {amount},"
                                f"{user_balance},"
                                f" '{constant.REMARK_RECEIVE.format(amount=amount, receive=self.__account_number)}');")
            self.db.commit()
            self.balance_enquiry()
            print(constant.CUSTOM_FORMAT)
            print(f"Amount is Successfully Transaction from Your Account\n"
                  f"Receiver Name: {receiver_username.capitalize()}\nReceiver Account No: {receiver_account} ")
        except InsufficientBalanceError as ibe:
            print(ibe)
            return
        except AccountNotExist as ane:
            print(ane)
            return
        except OperationalError as e:
            print(constant.OPERATIONAL_ERROR, e)
            return
        except ProgrammingError as e:
            print(constant.PROGRAMMING_ERROR, e)
            return


if __name__ == "__main__":
    obj = Bank("mohit", 65823378)
    obj.transfer_funds(65823378, 5000)

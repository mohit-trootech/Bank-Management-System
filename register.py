"""User Registration Class Implement Signin Signup Methods"""
import constant
from customer import Customer
from database import BankingDatabase, OperationalError, ProgrammingError
from utils import generate_account_number, get_location, custom_print, AgeError, UserNotExist


class Registration(BankingDatabase):
    """
    class to implement User Registration Process
    """

    def __init__(self):
        super().__init__()

    def sign_up(self) -> bool:
        """
        user sign up method
        @return: bool
        """
        try:
            custom_print("Please Sign UP")
            username = input("Create Username: ")
            self.cursor.execute(f"SELECT username FROM customers where username = '{username}';")
            if self.cursor.fetchone():
                custom_print(constant.USERNAME_NOT_AVAILABLE)
                return False
            custom_print("Username Available Please Proceed")
            password = input("Enter Your Password: ")
            name = input("Enter Your Name: ")
            age = int(input("Enter Your Age (In Number Format): "))
            if age < 18:
                raise AgeError()
            pincode = input("Enter Your Pincode: ")
            while True:
                account_number = generate_account_number()
                self.cursor.execute(f"SELECT account_number FROM customers WHERE "
                                    f"account_number = '{account_number}';")
                if not self.cursor.fetchone():
                    break
            address = get_location(pincode)
            customer_obj = Customer(username, password, name, age, str(address), account_number)
            customer_obj.create_user()
            self.create_transaction_table(username)
            self.db.commit()
            custom_print("User Successfully Created")
            return True
        except AgeError as ae:
            print(ae)
            return False
        except ValueError as ve:
            print(ve)
            return False
        except OperationalError as oe:
            print(oe)
            return False
        except ProgrammingError as pe:
            print(pe)
            return False
        except Exception as err:
            print(err)
            return False

    def sign_in(self) -> str:
        """
        method to implement customer sign in if exist
        @return: str
        """
        try:
            custom_print("Please Sign IN")
            username = input("Enter Username: ")
            user_details = self.cursor.execute(f"SELECT * FROM customers "
                                               f"where username = '{username}';").fetchone()
            if not user_details:
                raise UserNotExist()
            print(constant.CUSTOM_FORMAT)
            print(f"Welcome {username.capitalize()}")
            while True:
                password = input("Enter Password: ")
                if password.lower() == 'c':
                    custom_print("Thank for Using Services")
                    return
                if user_details[2] == password:
                    print("Sign IN Successfully")
                    return user_details
                else:
                    print("Wrong Password Try Again Press C/c to Exit")
                    continue
        except UserNotExist as une:
            print(une)
            return
        except OperationalError as oe:
            print(constant.OPERATIONAL_ERROR, oe)
            return
        except ProgrammingError as pe:
            print(constant.PROGRAMMING_ERROR, pe)
            return
        except Exception as err:
            print(constant.UNKNOWN_ERROR, err)
            return


if __name__ == "__main__":
    obj = Registration()
    obj.sign_in()

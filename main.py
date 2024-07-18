import constant
from utils import custom_print
from register import Registration
from bank import Bank

# Main Banking Object
obj = Registration()
custom_print("Hello, World! Banking")


def main() -> None:
    """
    Main Banking Function
    @return: None
    """
    try:
        register = int(input("1. SignUp\n"
                             "2. SignIn: "))
        if register == 1 or register == 2:
            if register == 1:
                user_signup_status = obj.sign_up()
                if not user_signup_status:
                    return
                user_details = obj.sign_in()
                if not user_details:
                    return
            elif register == 2:
                user_details = obj.sign_in()
                if not user_details:
                    return
        print(constant.CUSTOM_FORMAT)
        facility = int(input("1. User Details\n"
                             "2. Balance Enquiry\n"
                             "3. Cash Credit\n"
                             "4. Cash Debit\n"
                             "5. Fund Transfer\n"
                             "6. Exit: "))
        bobj = Bank(user_details[1], user_details[-2])
        if 1 <= facility <= 6:
            if facility == 1:
                bobj.user_details()
            if facility == 2:
                bobj.balance_enquiry()
            elif facility == 3:
                amount = int(input("Enter Amount to Deposit: "))
                bobj.user_credit(amount)
            elif facility == 4:
                amount = int(input("Enter Amount to Withdraw: "))
                bobj.user_debit(amount)
            elif facility == 5:
                receive = int(input("Enter Receiver Account Number: "))
                amount = int(input("Enter Money to Transfer: "))
                bobj.transfer_funds(receive, amount)
            elif facility == 6:
                custom_print("Thanks For Using Banking Services")
        else:
            print(constant.VALID_INPUT)
    except ValueError:
        print(constant.VALUE_ERROR)


if __name__ == "__main__":
    """Banking Module Main"""
    main()

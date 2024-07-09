"""Python Files to Store Constants"""
from datetime import datetime

# Banking Constant
DB = "banking.db"

# Status Constant
STATUS_TRUE = 1
STATUS_FALSE = 0

CURRENT_TIME = datetime.now().replace(microsecond=0)

# Errors
OPERATIONAL_ERROR = "Error in SQL Execution"
PROGRAMMING_ERROR = "SQLITE Syntax Error Occurred"
UNKNOWN_ERROR = "Unknown Exception Occurred"
VALUE_ERROR = "Please Enter Number Input in Required Field"
VALID_INPUT = "Please Select Valid Input"

# Banking Error
USERNAME_NOT_AVAILABLE = "Username Not Available Try Creating a New One"
USER_CREATION_ERROR = "Sorry, Error Occurred in User Creation Try Again"
USER_NOT_EXIST = "User doesn't Exist"
BALANCE_NOT_AVAILABLE = "Balance is not Available for This Transaction"
ACCOUNT_NOT_EXIST = "Account Number Not Exist Please Check & Enter Correct Account Number "
LOC_ERROR = "Unable to Fetch Location Try Again"
PIN_ERROR = "Unable to Fetch Location From Pin Code"
AGE_ERROR = "Banking Valid Age is 18+"

# REMARKS
REMARK_DEBIT = "Amount Debit of RS {amount}"
REMARK_CREDIT = "Amount Credit of RS {amount}"
REMARK_TRANSFER = "Amount TRANSFER of RS {amount} to {transfer}"
REMARK_RECEIVE = "Amount RECEIVE of RS {amount} from {receive}"

# REPORT
CREDIT_SUCCESS = "Amount is Successfully Credited From Your Account"
DEBIT_SUCCESS = "Amount is Successfully Debited From Your Account"

# print format
CUSTOM_FORMAT = "".center(40, "-")

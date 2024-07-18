"""
Banking Utility File to Generate utility Information
"""
import random
import constant
from geopy import Nominatim
from functools import partial


class UserNotExist(BaseException):
    """
    Age Error for Banking
    """
    def __init__(self, msg=constant.USER_NOT_EXIST):
        super(UserNotExist, self).__init__(msg)


class AgeError(BaseException):
    """
    Age Error for Banking
    """
    def __init__(self, msg=constant.AGE_ERROR):
        super(AgeError, self).__init__(msg)


class InsufficientBalanceError(BaseException):
    """
    Custom Class for Insufficient Balance Exception
    """

    def __init__(self, msg=constant.BALANCE_NOT_AVAILABLE):
        super(InsufficientBalanceError, self).__init__(msg)


class AccountNotExist(BaseException):
    """
    Custom Class for Insufficient Balance Exception
    """

    def __init__(self, msg=constant.ACCOUNT_NOT_EXIST):
        super(AccountNotExist, self).__init__(msg)


class LocationError(Exception):
    """
    Custom Location Error Exception
    """

    def __init__(self, msg=constant.LOC_ERROR):
        super(LocationError, self).__init__(msg)


def generate_account_number() -> int:
    """
    function to generate account number
    @return: int
    """
    return random.randint(10000000, 99999999)


def custom_print(msg: str):
    print(msg.center(50, "-"))


def get_location_keyword(area: str) -> str:
    """
    function to get location based on area
    @param area: str
    @return:str
    """
    try:
        geolocate = Nominatim(user_agent="geoLocBanking")
        gecode = partial(geolocate.geocode)
        loc = gecode(area)
        if loc:
            return loc
        else:
            raise LocationError()
    except LocationError as le:
        print(le)
        return
    except Exception as err:
        print(constant.UNKNOWN_ERROR, err)
        return


def get_location(pin: str) -> str:
    """
    function to return location from pincode using 'geopy library'
    @param pin: str
    @return: str
    """
    try:
        geolocate = Nominatim(user_agent="geoLocBanking")
        loc = geolocate.geocode(pin)
        if loc:
            return loc
        else:
            print(constant.PIN_ERROR)
            area = input("Enter the Popular Area in Your Town/City: ")
            return get_location_keyword(area)
    except Exception as e:
        print(f"{constant.UNKNOWN_ERROR}: {e}")
        return


if __name__ == "__main__":
    print(get_location("307038"))

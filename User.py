import datetime as dt
import re
class User:

    #private variables
    __email_address = ''
    __password = ''
    __name = ''
    __date_registered = ''

    # static variables
    number_of_users = 0

    def __init__(self, email_address, name):
        print('pending initializer implementation')

    #getters
    def get_email_address(self):
        return self.__email_address

    def get_password(self):
        return self.__password

    def get_name(self):
        return self.__name

    def get_date_registered(self):
        return self.__date_registered

    #setters
    def set_email_address(self, email_address):
        regexPattern = re.compile(r'.*@.*\\..*')
        if not re.match(regexPattern, email_address):
            print('The email is not in the correct format.')
        else:
            self.__email_address = email_address
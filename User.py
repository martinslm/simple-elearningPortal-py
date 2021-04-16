import datetime as dt
from random import randint
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
        self.set_name(name)
        self.set_email_address(email_address)
        self.set_password(randint(0, 10000))
        self.set_date_registered(str(dt.datetime.today()))
        User.number_of_users += 1

    def print_user_details(self):
        print('==================================================')
        print('====================== USER ======================')
        print('==================================================')
        print('Name: {0:<50}'.format(self.__name))
        print('Email: {0:<50}'.format(self.__email_address))
        print('Password: {0:<50}'.format(self.__password))
        print('Date Registered: {0:<50}'.format(self.__date_registered))

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
        r = re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')
        if not r.match(email_address):
            raise Exception('The email is not in the correct format.')
        else:
            self.__email_address = email_address

    def set_name(self, name):
        if not name:
            raise Exception('The name cannot be null.')
        else:
            self.__name = name

    def set_password(self, password):
        self.__password = password

    def set_date_registered(self, date):
        self.__date_registered = date
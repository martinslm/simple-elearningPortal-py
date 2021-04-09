from User import User

class Student(User):

    #private variables
    __student_number = 0
    __programme_code = ''
    __programme_year = ''
    __student_type = ''
    __list_of_grades = ''


    def __init__(self, email_address, name):
        super().__init__(email_address,name)


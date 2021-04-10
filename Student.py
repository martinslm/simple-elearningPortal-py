from User import User

class Student(User):

    #private variables
    __student_number = 0
    __programme_code = ''
    __programme_year = ''
    __student_type = ''
    __list_of_grades = ''

    STUDENT_TYPES_LIST = ['fulltime', 'parttime']

    def __init__(self, email_address, name, student_number, programme_code, programme_year, student_type, list_of_grades):
        try:
            super().__init__(email_address,name)
            self.set_student_number(student_number)
            self.set_programme_code(programme_code)
            self.set_programme_year(programme_year)
            self.set_student_type(student_type)
            self.set_list_of_grades(list_of_grades)
        except Exception as ex:
            print(ex)

    #getters
    def get_student_number(self):
        return self.__student_number

    def get_programme_code(self):
        return self.__programme_code

    def get_programme_year(self):
        return self.__programme_year

    def get_student_type(self):
        return self.__student_type

    def get_list_of_grades(self):
        return self.__list_of_grades

    #setters
    def set_student_number(self, student_number):
        if not student_number.isnumeric() or len(student_number) != 9:
            raise Exception('Student number is in an incorrect format')
        else:
            self.__student_number = student_number

    def set_programme_code(self, programme_code):
        if not programme_code:
            raise Exception('The programme_code cannot be null.')
        else:
            self.__programme_code = programme_code

    def set_programme_year(self, programme_year):
        if int(programme_year) < 1 or int(programme_year) > 6:
            raise Exception('Programme Year must be a value between 1 and 6.')
        else:
            self.__programme_year = programme_year

    def set_student_type(self, student_type):
        if not student_type.lower() in self.STUDENT_TYPES_LIST:
            raise Exception('Student type must be fulltime or parttime')
        else:
            self.__student_type = student_type.lower()

    def set_list_of_grades(self, list_of_grades):
        self.__list_of_grades = list_of_grades

teste = Student("errado@certo.com", "larissa", "123475990", '1', "1", "parttime", "teste")
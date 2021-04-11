from User import User

class Lecturer(User):

    #private variables
    __staff_id = 0
    __speciality = ''
    __qualification = ''

    VALID_QUALIFICATIONS_LIST = ['ba', 'bsc', 'ma', 'msc', 'phd']

    def __init__(self, email_address, name, staff_id, speciality, qualification):
        try:
            super().__init__(email_address, name)
            self.set_staff_id(staff_id)
            self.set_speciality(speciality)
            self.set_qualification(qualification)
        except Exception as ex:
            print(ex)

    def print_lecturer_details(self):
        print('==================================================')
        print('==================== LECTURER ====================')
        print('==================================================')
        print('Name: {0:<50}'.format(self.__name))
        print('Email: {0:<50}'.format(self.__email_address))
        print('Password: {0:<50}'.format(self.__password))
        print('Date Registered: {0:<50}'.format(self.__date_registered))
        print('Staff Id: {0:<50}'.format(self.__staff_id))
        print('Speciality: {0:<50}'.format(self.__speciality))
        print('Qualification: {0:<50}'.format(self.__qualification))

    #getters
    def get_staff_id(self):
        return self.__staff_id

    def get_speciality(self):
        return self.__speciality

    def get_qualification(self):
        return self.__qualification

    #setters
    def set_staff_id(self, staff_id):
        if not staff_id.isnumeric() or len(staff_id) != 6:
            raise Exception('Staff id is in an incorrect format')
        else:
            self.__staff_id = staff_id

    def set_speciality(self, speciality):
        if not speciality:
            raise Exception('The speciality cannot be null.')
        else:
            self.__speciality = speciality

    def set_qualification(self, qualification):
        if not qualification.lower() in self.VALID_QUALIFICATIONS_LIST:
            raise Exception('Qualification type must be ba, bsc, ma, msc or phd')
        else:
            self.__qualification = qualification.lower()
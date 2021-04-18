from Lecturer import Lecturer
from Student import Student

class Module:

    #private variables
    __module_id = 0
    __module_name = 'Unknown'
    __course_code = 0
    __department = 'Computing'
    __lecturer = ''
    __student_class_list = ''
    __assessment_list = ''

    VALID_DEPARTMENTS_LIST = ['computing', 'science', 'marketing', 'business', 'art']

    def __init__(self, module_id, module_name, course_code, department, lecturer):
        self.set_module_id(module_id)
        self.set_module_name(module_name)
        self.set_course_code(course_code)
        self.set_department(department)
        self.set_lecturer(lecturer)
        self.__student_class_list = []
        self.__assessment_list = []

    #getters
    def get_module_id(self):
        return self.__module_id

    def get_module_name(self):
        return self.__module_name

    def get_course_code(self):
        return self.__course_code

    def get_department(self):
        return self.__department

    def get_lecturer(self):
        return self.__lecturer

    def get_student_class_list(self):
        return self.__student_class_list

    def get_assessment_list(self):
        return self.__assessment_list

    #setters
    def set_module_id(self, module_id):
        if not module_id:
            raise Exception('Module Id cannot be null')
        else:
             self.__module_id = int(module_id)

    def set_module_name(self, module_name):
        self.__module_name = module_name

    def set_course_code(self, course_code):
        self.__course_code = int(course_code)

    def set_department(self, department):
        if not department.lower() in self.VALID_DEPARTMENTS_LIST:
            raise Exception('The department should be invalid.')
        else:
            self.__department = department.lower()

    def set_lecturer(self, lecturer):
        if isinstance(lecturer, Lecturer):
            self.__lecturer = lecturer
        else:
            raise Exception('The lecturer is not a valid object')

    def set_student_class_list(self, student_class_list):
        self.__student_class_list = student_class_list

    def set_assessment_list(self, assessment_list):
        self.__assessment_list = assessment_list

    #methods
    def auto_add_class_list(self, file_name):
        with open(file_name, 'r') as file:
            for line in file:
                line_of_array = line.split(';')
                student_object = Student(line_of_array[0], line_of_array[2], line_of_array[4], line_of_array[5], line_of_array[6], line_of_array[7], line_of_array[8])
                student_object.set_password(line_of_array[1])
                student_object.set_date_registered(line_of_array[3])
                self.__student_class_list.append(student_object)

    def append_to_assessment_list(self, assessment_1d_format):
        self.__assessment_list.append(assessment_1d_format)

    def append_to_class_list(self, student):
        if isinstance(student, Student):
            self.__student_class_list.append(student)
        else:
            raise Exception('Invalid Object')

    def print_module_details(self):
        print('=======================================================================================')
        print('====================================== MODULE =========================================')
        print('=======================================================================================')
        print('Module Id: {0:<50}'.format(self.__module_id))
        print('Module Name: {0:<50}'.format(self.__module_name))
        print('Course Code: {0:<50}'.format(self.__course_code))
        print('Department: {0:<50}'.format(self.__department))
        print('Lecturer:')
        print('\tEmail Address: {0:<50}' .format(self.__lecturer.get_email_address()))
        print('\tName: {0:<50}'.format(self.__lecturer.get_name()))
        print('\tStaff Id: {0:<50}'.format(self.__lecturer.get_staff_id()))
        print('\tSpeciality: {0:<50}'.format(self.__lecturer.get_speciality()))
        print('\tQualification: {0:<50}'.format(self.__lecturer.get_qualification()))
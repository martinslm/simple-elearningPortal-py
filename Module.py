from Lecturer import Lecturer

class Module:

    #private variables
    __module_id = 0
    __module_name = 'Unknown'
    __course_code = 0
    __department = 'Computing'
    __lecturer = ''
    __student_class_list = []
    __assessment_list = []

    VALID_DEPARTMENTS_LIST = ['computing', 'science', 'marketing', 'business', 'art']

    def __init__(self, module_id, module_name, course_code, department, lecturer):
        self.set_module_id(module_id)
        self.set_module_name(module_name)
        self.set_course_code(course_code)
        self.set_department(department)
        self.set_lecturer(lecturer)

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
             self.__module_id = module_id

    def set_module_name(self, module_name):
        self.__module_name = module_name

    def set_course_code(self, course_code):
        self.__course_code = course_code

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
    def auto_add_class_list(self, fileName):
        with open(fileName, 'r') as file:
            for line in file:
                student_object = line.split(',')
                self.__student_class_list.append(student_object)

    def append_to_assessment_list(self, assessment_1d_format):
        self.__assessment_list.append(assessment_1d_format)

    def print_module_details(self):
        print('=======================================================================================')
        print('====================================== MODULE =========================================')
        print('=======================================================================================')
        print('Module Id: {0:<50}'.format(self.__module_id))
        print('Module Name: {0:<50}'.format(self.__module_name))
        print('Course Code: {0:<50}'.format(self.__course_code))
        print('Department: {0:<50}'.format(self.__department))
        print('Lecturer:')
        print('     Email Address: {0:<50}' .format(self.__lecturer.get_email_address()))
        print('     Name: {0:<50}'.format(self.__lecturer.get_name()))
        print('     Staff Id: {0:<50}'.format(self.__lecturer.get_staff_id()))
        print('     Speciality: {0:<50}'.format(self.__lecturer.get_speciality()))
        print('     Qualification: {0:<50}'.format(self.__lecturer.get_qualification()))
        print('Students in Class: ')
        for i in range(len(self.__student_class_list)):
            print(' ')
            print('     Email: ' .format(self.__student_class_list[i][0]))
            print('     Name: '.format(self.__student_class_list[i][2]))
            print('     Date Registered: '.format(self.__student_class_list[i][3]))
            print('     Student Number: '.format(self.__student_class_list[i][4]))
            print('     Programme Code: '.format(self.__student_class_list[i][5]))
            print('     Programme Year: '.format(self.__student_class_list[i][6]))
            print('     Student Type: '.format(self.__student_class_list[i][7]))
            print('     List of Grades: '.format(self.__student_class_list[i][8]))
        print('Assessment List:')
        for i in range(len(self.__assessment_list)):
            print(' ')
            print('     Student Number: ' .format(self.__assessment_list[i][0]))
            print('     Assessment Name: '.format(self.__assessment_list[i][1]))
            print('     Percentage Achieved: '.format(self.__assessment_list[i][2]))
            print('     Grade Achieved: '.format(self.__assessment_list[i][3]))
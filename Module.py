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
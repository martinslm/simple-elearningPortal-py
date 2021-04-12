class Module:

    #private variables
    __module_id = 0
    __module_name = 'Unknown'
    __course_code = 0
    __department = 'Computing'
    __lecturer = ''
    __student_class_list = ''
    __assessment_list = ''

    def __init__(self, module_id, module_name, course_code, department, lecturer):
        self.set_module_id(module_id)
        self.set_module_name(module_name)
        self.set_course_code(course_code)
        self.set_department(department)
        self.set_lecturer(lecturer)

      #Para terminar itens 6:  Deve inicializar as variáveis apenas se os dados do parâmetro forem válidos, ou seja:
      #  i.O module_id não deve ficar em branco.
      #  ii.O departamento pode ser Computação / Ciência / Marketing / Negócios / Arte
      #  iii.O palestrante __lecturer deve ser um objeto Palestrante.
      #  d) As listas: class_list e assessment_list devem ser inicializadas com listas vazias.

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

    def set_module_id(self, module_id):
        self.__module_id = module_id

    def set_module_name(self, module_name):
        self.__module_name = module_name

    def set_course_code(self, course_code):
        self.__course_code = course_code

    def set_department(self, department):
        self.__department = department

    def set_lecturer(self, lecturer):
        self.__lecturer = lecturer

    def set_student_class_list(self, student_class_list):
        self.__student_class_list = student_class_list

    def set_assessment_list(self, assessment_list):
        self.__assessment_list = assessment_list
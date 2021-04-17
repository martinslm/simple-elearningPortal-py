from Module import Module
from Lecturer import Lecturer
from Student import Student
import GradeCalculator as gc

option = 1
lecturerTest = Lecturer('email@lecturer.com', 'Lecturer of art', '123456', 'dance', 'phd')
moduleTest = Module('1','Art','10','Art', lecturerTest)
moduleTest2 = Module('2','Art','10','Art', lecturerTest)
list_of_modules = [moduleTest, moduleTest2]

from User import User
userTest = User('email@user.com', 'test')
userTest.set_password('23')
userTest.print_user_details()

#MENU FUNCTIONS
def add_module():
    module_id = int(input('Enter the module Id: '))
    containsId = any((module.get_module_id() == module_id) for module in list_of_modules)
    if containsId:
        print('ATTENTION: There is already a module registered in the system for this Id.')
    else:
        module_name = input('Enter the module Name: ')
        course_code = input('Enter the course Code: ')
        department = input('Enter the department: ')
        email_address_lecturer = input('Enter the lecturer email address: ')
        name_lecturer = input('Enter the lecturer name: ')
        staff_id_lecturer = input('Enter the lecturer staff id: ')
        speciality_lecturer = input('Enter the lecturer speciality: ')
        qualification_lecturer = input('Enter the lecturer qualification: ')
        lecturer = Lecturer(email_address_lecturer, name_lecturer, staff_id_lecturer, speciality_lecturer, qualification_lecturer)
        module = Module(module_id, module_name, course_code, department, lecturer)
        list_of_modules.append(module)

def add_students_to_module():
    module_id = int(input('Enter the module Id: '))
    containsId = any((module.get_module_id() == module_id) for module in list_of_modules)
    if not containsId:
        print('Module not found')
    else:
        moduleForAddUsers = [module for module in list_of_modules if module.get_module_id() == module_id]
        for item in moduleForAddUsers:
            moduleObject = item
        selectedWay = input('How do you want to add students? \n Select 1 for a file \n Select 2 for manual mode \n Others inputs return for the menu\n')
        if selectedWay == '1':
            fileName = input('Enter the file: ')
            moduleObject.auto_add_class_list(fileName)
        elif selectedWay == '2':
            email_address = input('Enter the email address: ')
            name = input('Enter the user name: ')
            student_number = input('Enter the student number: ')
            programme_code = input('Enter the programme code: ')
            programme_year = input('Enter the programme year: ')
            student_type = input('Enter the student type: ')
            list_of_grades = input('Enter the list of grades: ')
            student = Student(email_address, name, student_number, programme_code, programme_year, student_type, list_of_grades)
            student.print_student_details()
            moduleObject.append_to_class_list(student)
        else:
            return

def add_students_grades_to_module():
    module_id = int(input('Enter the module Id: '))
    containsId = any((module.get_module_id() == module_id) for module in list_of_modules)
    if not containsId:
        print('Module not found')
    else:
        quantityOfGrades = int(input('How many grades you want to add?'))
        for i in range(quantityOfGrades):
            student_number = input('Enter the student number: ')
            assessment_name = input('Enter the assessment name: ')
            percentage_achieved = input('Enter the percentage achieved: ')
            grade_achieved = gc.GradeCalculator.calculate_grade(percentage_achieved)
            list1d = [student_number, assessment_name, percentage_achieved, grade_achieved]
            moduleForAddUsers = [module for module in list_of_modules if module.get_module_id() == module_id]
            for item in moduleForAddUsers:
                moduleObject = item
            moduleObject.append_to_assessment_list(list1d)

def display_all_modules():
    for module in list_of_modules:
        module.print_module_details()

    print('\n')
    print('*** TOTAL NUMBER OF MODULES: {0} ****' .format(len(list_of_modules)))
    print('*** TOTAL NUMBER OF STUDENTS: {0} ****' .format()) #descobrir
    #Mostra a lista de todos os Módulos e no final irá mostrar:
    #• Número total de módulos no sistema. // Total number of modules in the system.
    #• Número total de alunos no sistema. // Total number of students in the system.
    #• Número total de módulos do sistema, por departamento. // Total number of modules in the system, by department.

def display_list_of_students():
    print("opcao 5 selecionado")

def display_list_of_students_grades():
    print("opcao 6 selecionada")

def exit():
    print('bye bye')

#MENU
while option != 7:
    print("\n")
    print("*************************************************************************")
    print("*                                Menu                                   *")
    print("*                          1) Add module                                *")
    print("*                     2) Add students to Module                         *")
    print("*                  3) Add student grades to Module:                     *")
    print("*   4) Display list of all Modules and at the end it will display:      *")
    print("*                   5) Display list of Students                         *")
    print("*                6) Display list of Students Grades                     *")
    print("*                               7) Exit                                 *")
    print("*************************************************************************")
    option = input("Enter option: ")
    print("\n")

    try:
        if option.isdigit():
            option = int(option)

            if option == 1:
                add_module()
            elif option == 2:
                add_students_to_module()
            elif option == 3:
                add_students_grades_to_module()
            elif option == 4:
                display_all_modules()
            elif option == 5:
                display_list_of_students()
            elif option == 6:
                display_list_of_students_grades()
            elif option == 7:
                exit()
            else:
                print("Invalid number option entered - try again (number between 1 and 7)")
        else:
            print("Error, you did not enter a valid option - try again (number between 1 and 7).\n")
    except Exception as err:
        print('\n')
        print('We were unable to process your request')
        print(err)
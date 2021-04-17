from Module import Module
from Lecturer import Lecturer
from Student import Student
import GradeCalculator as gc

option = 1
lecturerTest = Lecturer('email@lecturer.com', 'Lecturer of art', '123456', 'dance', 'phd')
moduleTest = Module('1','Art','10','Art', lecturerTest)
moduleTest2 = Module('2','Art','10','Art', lecturerTest)
list_of_modules = [moduleTest, moduleTest2]

#MENU FUNCTIONS
def add_module():
    module_id = int(input('Enter the module Id: '))
    contains_id = any((module.get_module_id() == module_id) for module in list_of_modules)
    if contains_id:
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
    contains_id = any((module.get_module_id() == module_id) for module in list_of_modules)
    if not contains_id:
        print('Module not found')
    else:
        module_for_add_users = [module for module in list_of_modules if module.get_module_id() == module_id]
        for item in module_for_add_users:
            module_object = item
        selected_way = input('How do you want to add students? \n Select 1 for a file \n Select 2 for manual mode \n Others inputs return for the menu\n')
        if selected_way == '1':
            file_name = input('Enter the file: ')
            module_object.auto_add_class_list(file_name)
            print('Sucess to insert')
        elif selected_way == '2':
            email_address = input('Enter the email address: ')
            name = input('Enter the user name: ')
            student_number = input('Enter the student number: ')
            programme_code = input('Enter the programme code: ')
            programme_year = input('Enter the programme year: ')
            student_type = input('Enter the student type: ')
            list_of_grades = input('Enter the list of grades: ')
            student = Student(email_address, name, student_number, programme_code, programme_year, student_type, list_of_grades)
            module_object.append_to_class_list(student)
            print('Sucess to insert')
        else:
            return

def add_students_grades_to_module():
    module_id = int(input('Enter the module Id: '))
    contains_id = any((module.get_module_id() == module_id) for module in list_of_modules)
    if not contains_id:
        print('Module not found')
    else:
        quantity_of_grades = int(input('How many grades you want to add?'))
        for i in range(quantity_of_grades):
            student_number = input('Enter the student number: ')
            assessment_name = input('Enter the assessment name: ')
            percentage_achieved = input('Enter the percentage achieved: ')
            grade_achieved = gc.GradeCalculator.calculate_grade(percentage_achieved)
            list1d = [student_number, assessment_name, percentage_achieved, grade_achieved]
            module_for_add_users = [module for module in list_of_modules if module.get_module_id() == module_id]
            for item in module_for_add_users:
                module_object = item
            module_object.append_to_assessment_list(list1d)

def display_all_modules():
    total_students = 0
    departments = [];
    for module in list_of_modules:
        module.print_module_details()
        total_students += len(module.get_student_class_list())
        departments = module.VALID_DEPARTMENTS_LIST
    print('\n')
    print('*** TOTAL NUMBER OF MODULES: {0} ****' .format(len(list_of_modules)))
    print('*** TOTAL NUMBER OF STUDENTS: {0} ****' .format(total_students))
    for department in departments:
        department_count = len([module for module in list_of_modules if module.get_department() == department])
        print('*** TOTAL NUMBER OF MODULES WITH {0} DEPARTMENT: {1} ****'.format(department.upper(), department_count))

def display_list_of_students():
    module_id = int(input('Enter the module Id: '))
    contains_id = any((module.get_module_id() == module_id) for module in list_of_modules)
    if not contains_id:
        print('Module not found')
    else:
        module_for_list_students = [module for module in list_of_modules if module.get_module_id() == module_id]
        for module in module_for_list_students:
            total_students = len(module.get_student_class_list())
            for student in module.get_student_class_list():
                student.print_student_details()
            print('*** TOTAL STUDENTS IN MODULE {0}: {1} ***' .format(module.get_module_id(), total_students))

def display_list_of_students_grades():
    module_id = int(input('Enter the module Id: '))
    contains_id = any((module.get_module_id() == module_id) for module in list_of_modules)
    if not contains_id:
        print('Module not found')
    else:
        module_for_list_assessment = [module for module in list_of_modules if module.get_module_id() == module_id]
        for module in module_for_list_assessment:
            assessment_list = module.get_assessment_list()
            total = len(assessment_list)
            highest_percentage = max(int(percentage) for percentage in assessment_list[2])
            lowest_percentage = min(int(percentage) for percentage in assessment_list[2])
            average_percentage = sum(int(percentage) for percentage in assessment_list[2]) / total
            for assessment in assessment_list:
                print('**********************************')
                print('*********** ASSESSMENT ***********')
                print('**********************************')
                print('     Student Number: {0}'.format(assessment[0]))
                print('     Assessment Name: {0}'.format(assessment[1]))
                print('     Percentage Achieved: {0}'.format(assessment[2]))
                print('     Grade Achieved: {0}'.format(assessment[3]))

            print('**************************************')
            print('********* GENERAL INFORMATIONS *******')
            print('**************************************')

            print('Total: {0}' .format(total))
            print('Highest: {0}' .format(highest_percentage))
            print('Lowest: {0}'.format(lowest_percentage))
            print('Average: {0}' .format(average_percentage))
            grades = ['A', 'B+', 'B', 'B-', 'C+', 'C', 'D', 'F']
            for grade in grades:
                students_in_grade = len([assessment for assessment in module.get_assessment_list() if assessment[3] == grade])
                print('{0}: {1} students' .format(grade, students_in_grade))

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
from Module import Module
from Lecturer import Lecturer
#### Meta amanha:
#### Ler o arquivo Modules.csv e armazenar todos os registros em uma lista de modulos no main program.
#### Fazer todas as ações do item i. Add Module
#POSSIBILIDADE DE TRANSFORMAR MENU EM SWITCH CASE
option = 1
lecturerTest = Lecturer('email@lecturer.com', 'Lecturer of art', '123456', 'dance', 'phd')
moduleTest = Module('1','Art','10','Art', lecturerTest)
list_of_modules = [moduleTest]

from User import User
userTest = User('email@user.com', 'test')
userTest.set_password('23')
userTest.print_user_details()

#MENU FUNCTIONS
def add_module():
    module_id = int(input('Informe the module Id: '))
    containsId = any((module.get_module_id() == module_id) for module in list_of_modules)
    if containsId:
        print('ATTENTION: There is already a user registered in the system for this Id.')
    else:
        print('PEDIR O RESTANTE DOS DADOS PELO INPUT, CRIAR UM MODULE OBJECT E ADICIONAR O MODULO A LISTA.')

def add_students_to_module():
    print('opcao 2 selecionada')

def add_students_grades_to_module():
    print('opcao 3 selecionada')

def display_all_modules():
    print('opcao 4 selecionada')

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
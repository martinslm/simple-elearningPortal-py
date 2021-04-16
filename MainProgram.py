#### Meta amanha:
#### Ler o arquivo Modules.csv e armazenar todos os registros em uma lista de modulos no main program.
#### Fazer todas as ações do item i. Add Module
#POSSIBILIDADE DE TRANSFORMAR MENU EM SWITCH CASE
option = 1

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
            print('opcao 1 selecionada')
            #chamar metodo que será criado add Module
        elif option == 2:
            print('opcao 2 selecionada')
        elif option == 3:
            print('opcao 3 selecionada')
        elif option == 4:
            print('opcao 4 selecionada')
        elif option == 5:
            print("opcao 5 selecionado")
        elif option == 6:
            print("opcao 6 selecionada")
        elif option == 7:
            print('bye bye')
        else:
            print("Invalid number option entered - try again (number between 1 and 7)")
    else:
        print("Error, you did not enter a valid option - try again (number between 1 and 7).\n")
def help():
    print("\nadd - добавить заметку\nread - чтение заметки (+ -a - чтение всех заметок)\nhelp - список сущестующих команд(+ -a - все команды, включая ком. разработчика)\ntoff - (turn off) выключить приложение 'Заметки'\nrm - (remove) удалить заметку")



# def toff(status): #toff реалезован в User/Menu.py
#     asses = input("Вы хотите закрыть 'Заметки'? [Yes/Not]")

#     if asses == "Yes" or asses == "Y" or asses == "y" or asses == "yes":
#         status = False

#     elif asses == "Not" or asses == "N" or asses == "n" or asses == "not":
#         return
    
#     else:
#         print("Некорректный ответ")



def chcst(status): #(check_status) - команда разработчика
    print()
    print(status)
    print()

def help_a(): #all help(commands)
    print("\nadd - добавить заметку\nread - чтение заметки (+ -a - чтение всех заметок)\nhelp - список сущестующих команд\ntoff - (turn off) выключить приложение 'Заметки'\nchcst - проверка статуса приложения\n")

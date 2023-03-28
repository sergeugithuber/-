from Core.Act import add, read, readAll, remove
from Core.CommandForMenu import help, chcst, help_a

def start():
    machine = True #machine is turned on 
    
    while machine != False:
        command = input("Введите команду: ")

        if command == "add":
            add()

        elif command == "read":
            read()

        elif command == "help":
            help()
        
        elif command == "toff":
            # toff(machine)
            machine = False
        
        elif command == "rm":
            remove()
        
        elif command == "read -a":
            readAll()
        
        elif command == "chcst":
            chcst(machine)

        elif command == "help -a":
            help_a()

        else:
            print(f'" {command} "такой команды нет. help - список команд')
        
        
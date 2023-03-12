from random import randint
from time import ctime
import datetime

array_id = []
file = "note.txt"
fileForRemove = "data.txt"
cod = "utf-8"

def add ():
    head = input("Заголовок: \n")
    put = input("Ввод: \n")
    save = input("Save? [Yes/Not]: ")

    if save == "Y" or save == "YES" or save == "y" or save == "yes" or save == "Yes":
        time = datetime.datetime.now()
        id = randint(10000, 99999)
        if id in array_id:
            while True:
                id = randint(10000, 99999)
                if id not in array_id:
                    array_id.append(id)
                    break
        print("yuor id: " + str(id))

        with open(file, "a", encoding=cod) as f:
            f.write(f"{str(id)}\n")
            f.write(f"{str(time)}\n")
            f.write(f"{head}\n")
            f.write(f"{put}\n")
            f.close
    elif save == "N" or save == "NOT" or save == "n" or save == "not" or save == "Not":
        print("Отменено")
    else:
        print("not find command: " + save)


def read():
    search = input("How to search? [id]: ")
    
    if search == "id":

        find_id = input("your id: ") + "\n"
        count = 4
        asses = False 

        with open(file, "r", encoding=cod) as f:
            for line in f:
                if line == find_id:
                    asses = True #начало чтения
                if asses == True:
                    print(line)
                    count -= 1
                    if count == 0:
                        f.close
                        break        
    # elif search == "head":
    #     find_head = input("your head: ") + "\n"
    #     save = ""
    #     asses = False

    #     with open(file, "r", encoding=cod) as f:
    #         for line in f:
    #             break
    else:
        print("некорректный ввод")
                
def readAll():
    with open(file, "r", encoding=cod) as f:
        for line in f:
            print(line)

def remove(): 
    id = input("your id: ") + "\n"
    asses = False
    count = 4


    f = open(file, "r", encoding=cod)
    w = open(fileForRemove, "w", encoding=cod)
    for line in f:

        if line == id:
            asses = True

        if asses == True:
            count -= 1

            if count == 0 or count == -1:
                asses = False
                continue

            continue
        w.write(line)
    
    f.close
    w.close

    f = open(file, "w", encoding=cod)
    w = open(fileForRemove, "r", encoding=cod)

    for line in w:
        f.write(line)

    f.close
    w.close

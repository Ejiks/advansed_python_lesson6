documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def doc_num(number):
    for num_key in documents:
        if num_key.get("number") == number:
            return num_key.get("name")

def doc_shelf(number):
    for shelf_list in directories:
        for num in directories[shelf_list]:
            if num == number:
                return shelf_list

def all_doc_list():
    doc_list = ""
    for key in documents:
        doc_str = list(key.values())
        doc_list = f'{doc_list}\n{" ".join(doc_str)}'
        
    return doc_list

def add_doc (type, number, name, shelf):
    new_doc = {"type": type,"number": number, "name": name}
    documents.append(new_doc)
    new_doc_shelf = directories[shelf]
    new_doc_shelf.append(number)
    directories[shelf] = new_doc_shelf
    return documents, directories

def add_shelf(new_shelf_num):
    for key in directories:
        if key == new_shelf_num:
            return "Такая полка существует"
        else:
            directories[new_shelf_num] = []
        return directories

def moove_doc_shelf(number, new_shelf):
    for key in directories:
        for num in directories[key]:
            if num == number: 
                directories[key].remove(number)
                directories[new_shelf].append(number)
                return directories
        
def doc_delete(number):
    for num_key in documents:
        if num_key.get("number") == number:
            documents.remove(num_key)
    for shelf_list in directories:
        for num in directories[shelf_list]:
            if num == number:
                directories[shelf_list].remove(number)
    return directories, documents

def doc_shelf_validation(new_shelf):
    for key in list(directories.keys()):
        if key == new_shelf:
            return True
    return "Такой полки не существует"

def doc_number_validation(number):
    for num_list in list(directories.values()):
        for num in num_list:
            if num == number:
                return True
    return "Документ с таким номером не существует"
if __name__ == '__main__':
    user_command = input("Введите команду:\n p - people\n s – shelf\n l – list\n a – add\n d – delete\n m – move\n as – add shelf\n")
    if user_command == "p":
        #команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
        number = input("Введите номер документа:\n")
        if doc_number_validation(number) == True:
            print(f"Владелец кодкумента {doc_num(number)}")
        else:
            print(doc_number_validation(number))
    elif user_command == "s":
        #команда, которая спросит номер документа и выведет номер полки, на которой он находится;
        number = input("Введите номер документа:\n")
        if doc_number_validation(number) == True:
            print(f"Документ находится на полке номер {doc_shelf(number)}")
        else:
            print(doc_number_validation(number))
    elif user_command == "l":
        #команда, которая выведет список всех документов в формате Тип документа Номер документа Владелец документа;
        print(f"Ниже выведены все документы в формате: Тип документа Номер документа Владелец документа\n{all_doc_list()}")
    elif user_command == "a":
        #команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
        shelf = input("Введите полку для документа:\n")
        if doc_shelf_validation(shelf) != True:
                print(doc_shelf_validation(shelf))
        else:
            type = input("Введите название типа документа:\n")
            number = input("Введите номер документа:\n")
            name = input("Введите ФИО владельца документа:\n")
            add_doc (type, number, name, shelf)
            print(f"Документ успешно добавлен\nНиже выведены все документы в формате: Тип документа Номер документа Владелец документа\n{all_doc_list()}")
    elif user_command == "d":
        #команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
        number = input("Введите номер документа:\n")
        if doc_number_validation(number) == True:
            doc_delete(number)
            print(f"Документ успешно удален\nНиже выведены все документы в формате: Тип документа Номер документа Владелец документа\n{all_doc_list()}")
        else:
            print(doc_number_validation(number))        
    elif user_command == "m":
        #команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
        number = input("Введите номер документа:\n")
        if doc_number_validation(number) == True:
            new_shelf = input("Введите полку для документа:\n")
            if doc_shelf_validation(new_shelf) == True:
                moove_doc_shelf(number, new_shelf)
                print(f"Документ успешно перемещен на другую полку\nНиже выведены все полки:\n{directories}")
        else:
            print(doc_number_validation(number))
    elif user_command == "as":
        #команда, которая спросит номер новой полки и добавит ее в перечень.
        new_shelf_num = input("Введите номер новой полки:\n")
        add_shelf(new_shelf_num)
        print(f"Ниже выведены все полки:\n{directories}")
    else:
        print("Такой команды не существует!")


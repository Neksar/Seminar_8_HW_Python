def show_contact(): # все контакты в справочнике
    with open('data.txt', 'r+', encoding='utf-8') as file:
        book = file.read()
    return book

def input_firstname(): # Вводим имя
    first = input("Введи имя: ")
    remfname = first[1:]
    firstchar = first[0]
    return firstchar.upper() + remfname

def input_lastname(): # Вводим фамилию
    last = input("Введи фамилию: ")
    remlname = last[1:]
    firstchar = last[0]
    return firstchar.upper() + remlname

def new_contact(): # Создание нового контакта
    firstname = input_firstname()
    lastname = input_lastname()
    phoneNum = input("Введи телефон: ")
    contactDetails = ("["+firstname + " " + lastname +
                      ", " + phoneNum + "]\n")
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(contactDetails)
    print(contactDetails + "\nКонтакт успешно сохранён!")


def search_contact(): # Поиск контакта
    searchname = input("Введите имя для поиска: ")
    remname = searchname[1:]
    firstchar = searchname[0]
    searchname = firstchar.upper() + remname
    with open('data.txt', 'r+', encoding='utf-8') as file:
        filecontents = file.readlines()

    found = False
    for line in filecontents:
        if searchname in line:
            print("Результат:", end=" ")
            print(line)
            found = True
            break
    if found == False:
        print("Не найдено", searchname)

def change_person(): # Изменение контакта
    searchname = input("Какой контакт хотите изменить? ")
    remname = searchname[1:]
    firstchar = searchname[0]
    searchname = firstchar.upper() + remname
    with open('data.txt', 'r', encoding='utf-8') as file:
        file_contents = file.readlines()
        found = False
        for line in file_contents:
            if searchname in line:
                print(end=" ")
                print(line)
                found = True
                break
    with open("data.txt", "w", encoding='utf-8') as file:
        for lines in file_contents:
            if line.strip(" ") != lines:
                file.write(lines)
    firstname = input_firstname()
    lastname = input_lastname()
    phoneNum = input("Введи телефон: ")
    contactDetails = ("["+firstname + " " + lastname +
                      ", " + phoneNum + "]\n")
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(contactDetails)
    print(contactDetails + "\nКонтакт успешно сохранён!")
    
def delete_contact():
    searchname = input("Какое имя хотите удалить? ")
    remname = searchname[1:]
    firstchar = searchname[0]
    searchname = firstchar.upper() + remname
    with open('data.txt', 'r', encoding='utf-8') as file:
        file_contents = file.readlines()
        found = False
        for line in file_contents:
            if searchname in line:
                print("Удалено:", end=" ")
                print(line)
                found = True
                break
    with open("data.txt", "w", encoding='utf-8') as file:
        for lines in file_contents:
            if line.strip(" ") != lines:
                file.write(lines)

def main_menu():
    print("\nМеню\n")
    print("1. Показать все контакты")
    print("2. Добавить новый контакт")
    print("3. Поиск контакта")
    print("4. Изменение контакта")
    print("5. Удаление контакта")
    print("6. Выход")
    choice = input("Введи нужное: ")
    if choice == "1":
        print(show_contact())
    elif choice == "2":
        print(new_contact())
    elif choice == "3":
        print(search_contact())
    elif choice == "4":
        change_person()
    elif choice == "5":
        delete_contact()    
    elif choice == "6":
        print("До свидания!")
    else:
        print("Пожалуйста, предоставьте действительные данные!\n")
        enter = input("Нажмите Enter, чтобы продолжить ...")
        main_menu()

main_menu()
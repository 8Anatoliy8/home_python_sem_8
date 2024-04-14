from allprint import print_all
from addcont import add_contact
from find import find_contact
from copycont import copy_contacts

def start_menu():
    menu_number = None
    while menu_number != 5:
        menu_number = int(input("Добро пожаловать в справочник!\n"
                            "Перечень функций:\n"
                            "1. Добавить контакт\n"
                            "2. Показать всю книгу\n"
                            "3. Поиск контакта по фамилии\n"
                            "4. Копировать контакт\n"
                            "5. Выход\n"
                            "Введите номер функции: "))
        menu_number = check_menu_number(menu_number)
        if menu_number == 1:
            add_contact()
        elif menu_number == 2:
            print_all()
        elif menu_number == 3:
            find_contact()
        elif menu_number == 4:
            copy_contacts()
    print("Пока, приходите еще!")
    
    
def check_menu_number(n):
    while n < 1 or n > 5:
        n = int(input("Ошибка! Введите цифру от 1 до 6\n"
                      "Перечень функций:\n"
                      "1. Добавить контакт\n"
                      "2. Показать всю книгу\n"
                      "3. Поиск контакта по фамилии\n"
                      "4. Копировать контакт\n"
                      "5. Выход\n"
                      "Введите номер функции: "))
    return n
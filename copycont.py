from addcont import print_all



def copy_contacts():
    print_all()
    choice_1 = input("Выберите справочник из которого хотите копировать (1 или 2): ")
    while choice_1 not in ['1', '2']:
        choice_1 = input("Ошибка! Выберите справочник 1 или 2: ")
    choice_2 = input("Выберите справочник в который хотите копировать (1 или 2): ")
    while choice_2 not in ['1', '2']:
        choice_2 = input("Ошибка! Выберите справочник 1 или 2: ")
    choice_contact = int (input("Выберите номер строки, которую хотите копировать: "))
    with open(f'DATA/data_{choice_1}.txt', 'r', encoding='utf-8') as file_1:
            lines = file_1.readlines()
            if not lines:
                print("Файл пуст.")
            if choice_contact < 1 or choice_contact > len(lines):
                print("Недопустимый номер строки.")
                return
            contact = lines[choice_contact - 1]
            with open(f'DATA/data_{choice_2}.txt', 'a', encoding='utf-8') as file_2:
                file_2.write(contact + '\n')
            print("Контакт успешно скопирован.")
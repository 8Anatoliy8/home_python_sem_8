from allprint import print_all


def add_contact():
    first_name = input ('Введите имя контакта: ')
    last_name = input ('Введите фамилию контакта: ')
    phone_number = input ('Введите номер телефона: ')
    data, choice = data_file()
    number_row = len(data) + 1
    with open(f'DATA/data_{choice}.txt', 'a', encoding='utf-8') as file:
        file.write(f'{number_row};{first_name};'
                   f'{last_name};{phone_number}\n')
    print ('Контакт успешно добавлен')
    
def choice_data():
    print_all()
    number = int (input ('Выберите справочник.\n'
                         'Для этого введите 1 или 2: '))
    while number < 1 or number > 2:
        number = int (input ('Ошибка! Нужно ввести 1 или 2:'))
    return number

def data_file():
    choice = choice_data()
    with open(f'DATA/data_{choice}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data, choice

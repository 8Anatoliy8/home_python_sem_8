
def print_all ():
    for i in range (1, 3):
        with open (f'DATA/data_{i}.txt', 'r', encoding = 'utf-8') as file:
            data = file.readlines()
        print (f'Контакты из {i} справочника: \n'
               f'{" ".join(data)}')
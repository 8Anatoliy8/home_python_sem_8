

def find_contact():
    s_name = input("Введите фамилию: ")
    n_line = []
    choice = input("Выберите справочник (1 или 2): ")
    while choice not in ['1', '2']:
        choice = input("Ошибка! Выберите справочник 1 или 2: ")
    with open (f'DATA/data_{choice}.txt', 'r', encoding='utf-8') as file:
        for counter, line in enumerate(file):
            line = line.split()
            if s_name in line[0]:
                n_line.append(counter)
                print("\t\t".join(line))

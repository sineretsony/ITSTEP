import json
from datetime import datetime

# Задание 1

countries_capitals = {
    'Украина': 'Киев',
    'США': 'Вашингтон',
    'Франция': 'Париж'
}


def addInfo(dict_data, new_country, capital):
    if new_country not in dict_data:
        dict_data[new_country] = capital
    else:
        print(f"Странa {new_country} уже есть в словаре.")
    return dict_data


def delInfo(dict_data, del_country):
    if del_country in dict_data:
        del dict_data[del_country]
    else:
        print(f"Страны {del_country} нет в словаре.")
    return dict_data


def searchInfo(dict_data, search_country):
    if search_country in dict_data:
        return dict_data[search_country]
    else:
        return "Страна не найдена."


def editInfo(dict_data, country, new_capital):
    if country in dict_data:
        dict_data[country] = new_capital
    else:
        print(f"Страны {country} нет в словаре.")
    return dict_data


def saveInfo(dict_data, filename):
    filename += '.json'
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(dict_data, file)


def loadInfo(filename):
    with open(filename, 'r') as file:
        dict_data = json.load(file)
    return dict_data


print(countries_capitals)
print(addInfo(countries_capitals, 'Украина', 'Гданск'))
print(delInfo(countries_capitals, 'США'))
print(searchInfo(countries_capitals, 'Польша'))
print(editInfo(countries_capitals, 'Польша', 'Варшава'))
saveInfo(countries_capitals, 'test2')
print(loadInfo('test2'))


# Задание 2

def create_new_file(file_name):
    print('Файл не был найден, будет создан новый файл', file_name)
    try:
        with open(file_name, 'w') as file:
            json.dump('', file)
        print('Файл успешно создан')
        return {}
    except Exception as a:
        print(f"Ошибка создания файла {a}")
        return {}


def open_work_file(file_name):
    file_name += '.json'
    try:
        print('Загрузка файла', file_name)
        with open(file_name, 'r') as file:
            data_office = json.load(file)
            print('Загрузка успешно завершена')
            return dict(data_office)
    except FileNotFoundError:
        return create_new_file(file_name)


def save_data_to_file(file_name, data):
    file_name += '.json'
    try:
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)
            print('Данные успешно сохранены в файл', file_name)
    except Exception as a:
        print(f"Ошибка сохранения файла {a}")


def add_employee(data):
    current_year = datetime.now().year
    print("Добавление нового сотрудника:")
    first_name = input("Введите имя: ").lower()
    last_name = input("Введите фамилию: ").lower()
    age = current_year - int(input("Введите год рождения: "))
    employee = {"first_name": first_name, "last_name": last_name, "age": age}
    data[last_name] = employee
    print("Сотрудник успешно добавлен.")


def edit_employee(data):
    current_year = datetime.now().year
    print("Изменение/Добавление сотрудника:")

    last_name_to_edit = input("Введите фамилию сотрудника: ")

    if last_name_to_edit in data:
        print("Сотрудник найден.")
        first_name = input("Введите новое имя: ").lower()
        new_last_name = input("Введите новую фамилию: ").lower()
        age = current_year - int(input("Введите новый год рождения: "))
        data.pop(last_name_to_edit)
        data[new_last_name] = {"first_name": first_name,
                               "last_name": new_last_name,
                               "age": age}

        print("Данные сотрудника успешно отредактированы.")
    else:
        print("Сотрудники с указанной фамилией не найдены.")


def delete_employee(data):
    print("Удаление сотрудника:")
    last_name_to_delete = input(
        "Введите фамилию сотрудника для удаления: ").lower()
    if last_name_to_delete in data:
        data.pop(last_name_to_delete)
        return
    print("Сотрудник с указанной фамилией не найден.")


def search_by_lastname(data):
    current_year = datetime.now().year
    print("Поиск сотрудника по фамилии:")
    last_name_to_search = input("Введите фамилию для поиска: ").lower()
    if last_name_to_search in data:
        print(f"Имя - {data[last_name_to_search]['first_name'].capitalize()}\n"
              f"Фамилия - {data[last_name_to_search]['last_name'].capitalize()}\n"
              f"Год рождения - {current_year - data[last_name_to_search]['age']}\n"
              f"Возраст - {data[last_name_to_search]['age']}")
    else:
        print("Сотрудники с указанной фамилией не найдены.")


def search_by_criteria(data):
    print('Поиск сотрудников по возрасту или начальной букве фамилии:')
    criteria_choice = input('Введите критерий: ').lower()
    st = False

    if criteria_choice.isdigit() and len(criteria_choice) < 3:
        criteria = int(criteria_choice)
        for k, v in data.items():
            if v["age"] == criteria:
                st = True
                print(f'Имя - {v["first_name"].capitalize()}\n'
                      f'Фамилия - {v["last_name"].capitalize()}\n'
                      f'Возраст - {v["age"]}')
        if not st:
            print('Нет сотрудников по таким критериям')
    elif criteria_choice.isalpha() and len(criteria_choice) == 1:
        criteria = criteria_choice.lower()
        for k, v in data.items():
            if v["last_name"].startswith(criteria):
                st = True
                print(f'Имя - {v["first_name"].capitalize()}\n'
                      f'Фамилия - {v["last_name"].capitalize()}\n'
                      f'Возраст - {v["age"]}')
        if not st:
            print('Нет сотрудников по таким критериям')
    else:
        print('Неверно введен критерий.')


def print_func():
    print('Добавления нового сотрудника       = 1')
    print('Редактирования сотрудника          = 2')
    print('Удаление сотрудника                = 3')
    print('Поиск по фамилии                   = 4')
    print('Вывод информации (возраст / буква) = 5')
    print('Сохранить данные                   = 9')
    print('Выход                              = 0')


def office():
    try:
        data_office = open_work_file('office')
    except:
        data_office = create_new_file('office.json')

    if len(data_office) < 1:
        print('Файл пустой, некоторые функции недоступны')
        status = False
    else:
        status = True
    if not status:
        print('Добавления нового сотрудника       = 1')
        print('Выход                              = 0')

    while True:
        if len(data_office) > 1:
            print_func()
        choice = input('Введите команду: ')
        if choice == '1':
            add_employee(data_office)
        elif choice == '2' and status:
            edit_employee(data_office)
        elif choice == '3' and status:
            delete_employee(data_office)
        elif choice == '4' and status:
            search_by_lastname(data_office)
        elif choice == '5' and status:
            search_by_criteria(data_office)
        elif choice == '9' and status:
            save_data_to_file('office', data_office)
        elif choice == '0':
            save_data_to_file('office', data_office)
            break
        else:
            print('Неверный выбор, попробуйте еще раз')


office()

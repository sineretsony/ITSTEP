from datetime import datetime

# Задание 4 классная
def createNewBook(file_name):
    try:
        if not file_name.endswith('.txt'):
            file_name += '.txt'

        with open(file_name, 'w+', encoding='utf-8') as file:
            print(f"Файл: {file_name} создан!")
    except Exception:
        print(f"Произошла ошибка при создании файла")


def addNewContact(file_name):
    try:
        if not file_name.endswith('.txt'):
            file_name += '.txt'

        newContact = input("Введите новый контакт: ")
        with open(file_name, 'a', encoding='utf-8') as contactBook:
            contactBook.write(newContact)
    except Exception:
        print(f"Произошла ошибка при добавлении контакта")


def openContactBook(file_name):
    try:
        if not file_name.endswith('.txt'):
            file_name += '.txt'

        with open(file_name, 'r', encoding='utf-8') as contact_book:
            data = contact_book.read()
            print("Содержимое записной книжки:")
            print(data)
    except Exception:
        print(f"Произошла ошибка при открытии записной книжки")


def deleteContact(file_name, contact_to_delete):
    if not file_name.endswith('.txt'):
        file_name += '.txt'

    try:
        with open(file_name, 'r', encoding='utf-8') as contact_book:
            lines = contact_book.readlines()

        with open(file_name, 'w', encoding='utf-8') as contact_book:
            for line in lines:
                if line.strip() != contact_to_delete:
                    contact_book.write(line)
        print("Контакт успешно удален.")
    except:
        print(f"Произошла ошибка при удалении контакта")


def contactBookFunc():
    file_name = None
    while True:
        print("Для создания записной книжки нажмите: 1")
        if file_name:
            print("Для добавления нового контакта нажмите: 2")
            print("Для удаления контакта нажмите: 3")
            print("Для открытия записной книжки нажмите: 4")
        else:
            print("Для открытия записной книжки нажмите: 0")
        print("Для выхода нажмите: 9")

        choice = input("Введите команду: ")

        if choice == '1':
            file_name = input(
                "Введите имя файла для создания записной книжки: ")
            createNewBook(file_name)

        elif choice == '2':
            if not file_name:
                print("Сначала необходимо открыть записную книжку.")
            else:
                addNewContact(file_name)

        elif choice == '3':
            if not file_name:
                print("Сначала необходимо открыть записную книжку.")
            else:
                contact_to_delete = input("Введите контакт для удаления: ")
                deleteContact(file_name, contact_to_delete)

        elif choice == '4' and file_name:
            file_name = input("Введите имя новой записной книжки: ")
            createNewBook(file_name)

        elif choice == '0' and not file_name:
            file_name = input(
                "Введите имя файла для открытия записной книжки: ")
            openContactBook(file_name)

        elif choice == '9':
            break

        else:
            print(
                "Некорректный выбор. Пожалуйста, выберите доступную команду.")


contactBookFunc()


# Задание 1
def file_comparison(file1, file2):
    try:
        with (open(file1, 'r', encoding='utf-8') as f1,
              open(file2, 'r', encoding='utf-8') as f2):
            data1 = f1.readlines()
            data2 = f2.readlines()
    except:
        print("Ошибка, проверте существует ли файл")
        return None
    min_lines = min(len(data1), len(data2))

    for i in range(min_lines):
        if data1[i] != data2[i]:
            print("Несовпадающие строки:")
            print(f"Файл 1: {data1[i]}")
            print(f"Файл 2: {data2[i]}")

    if len(data1) != len(data2):
        print("В файлах разное количество строк.")
        print(f"Файл 1 строки: {len(data1)}")
        print(f"Файл 2 строки: {len(data2)}")


# Usage
file_comparison('dat2a.txt', 'data2.txt')


# Задание 2
def files_info(file):
    try:
        with (open(file, 'r', encoding='utf-8') as file,
              open('file_info', 'w', encoding='utf-8') as file_info):
            data = file.readlines()
            charsum = 0
            numbers = 0
            number_lines = len(data)
            for line in data:
                charsum += len(line)
                for i in line:
                    if i.isdigit():
                        numbers += 1
            file_info.write(f'Количество символов {charsum}\n'
                            f'Количество строк {number_lines}\n'
                            f'Количество цифр {numbers}')
    except:
        print("Произошла ошибка!")


files_info('data.txt')


# Задание 3
def del_end_lines(file):
    try:
        with (open(file, 'r', encoding='utf-8') as f,
              open('result', 'w', encoding='utf-8') as w):
            data = f.readlines()
            w.write(''.join(data[:-1]))

    except:
        print("Ошибка работы с файлами!")


del_end_lines('data.txt')


# Задание 4
def big_lines(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = f.readlines()
            result = max(data)
            print(result)
    except:
        print("Ошибка в работе с файлами!")


big_lines('data.txt')


# Задание 5


def add_entry(diary, entry):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_entry = f'{current_time}:\n{entry}\n{"-" * 25}\n'

    with open(diary, 'a', encoding='utf-8') as file:
        file.write(new_entry)
    print('Запись успешно добавлена.')


def view_entries(diary):
    try:
        with open(diary, 'r', encoding='utf-8') as file:
            entries = file.read()
            if entries:
                print(entries)
            else:
                print('Дневник пуст.')
    except FileNotFoundError:
        print('Дневник не существует или пуст.')


def notebook():
    diary = 'diary.txt'

    while True:
        print('Меню:')
        print('1. Добавить запись')
        print('2. Просмотреть записи')
        print('3. Выйти')

        choice = input('Выберите действие: ')
        if choice == '1':
            entry = input('Введите текст записи: ')
            add_entry(diary, entry)
        elif choice == '2':
            view_entries(diary)
        elif choice == '3':
            break
        else:
            print('Некорректный выбор. Пожалуйста, выберите действие снова.')


notebook()

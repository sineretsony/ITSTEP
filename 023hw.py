# Задание 1

def add_player(players):
    name = input("Введите имя баскетболиста: ")
    height = float(input("Введите рост (в см): "))
    players[name] = height
    return players, f"Баскетболист {name} добавлен."


def remove_player(players):
    name = input("Введите имя, которое нужно удалить: ")
    if name in players:
        del players[name]
        return players, f"Баскетболист {name} удален."
    else:
        return players, f"Баскетболист {name} не найден."


def search_player(players):
    name = input("Введите имя для поиска: ")
    if name in players:
        return players, f"Баскетболист {name} имеет рост {players[name]} см."
    else:
        return players, f"Баскетболист {name} не найден."


def update_player(players):
    name = input("Введите имя баскетболиста: ")
    if name in players:
        new_height = float(input("Введите новый рост баскетболиста: "))
        players[name] = new_height
        return players, f"Данные баскетболиста {name} обновлены."
    else:
        return players, f"Баскетболист {name} не найден."


def print_players(players):
    info = "Информация о баскетболистах:\n"
    for name, height in players.items():
        info += f"{name} - {height} см\n"
    return players, info


basketball_players = {}

while True:
    print("\nВыберите действие:")
    print("1. Добавить баскетболиста")
    print("2. Удалить баскетболиста")
    print("3. Найти баскетболиста")
    print("4. Обновить данные о баскетболисте")
    print("5. Вывести информацию о всех баскетболистах")
    print("6. Завершить программу")

    choice = input("Введите номер действия: ")

    if choice == '1':
        basketball_players, message = add_player(basketball_players)
        print(message)
    elif choice == '2':
        basketball_players, message = remove_player(basketball_players)
        print(message)
    elif choice == '3':
        basketball_players, message = search_player(basketball_players)
        print(message)
    elif choice == '4':
        basketball_players, message = update_player(basketball_players)
        print(message)
    elif choice == '5':
        basketball_players, message = print_players(basketball_players)
        print(message)
    elif choice == '6':
        break
    else:
        print("Некорректный выбор")


# Задание 2
def add_word(dictionary):
    english_word = input("Введите английское слово: ")
    french_translation = input("Введите перевод на французский: ")
    dictionary[english_word] = french_translation
    print("Слово добавлено в словарь.")


def remove_word(dictionary):
    english_word = input("Введите английское слово для удаления: ")
    if english_word in dictionary:
        del dictionary[english_word]
        print(f"Слово '{english_word}' удалено из словаря.")
    else:
        print(f"Слово '{english_word}' не найдено в словаре.")


def search_word(dictionary):
    english_word = input("Введите английское слово для поиска: ")
    if english_word in dictionary:
        print(f"Перевод слова '{english_word}': {dictionary[english_word]}")
    else:
        print(f"Слово '{english_word}' не найдено в словаре.")


def update_word(dictionary):
    english_word = input("Введите английское слово для обновления: ")
    if english_word in dictionary:
        new_french_translation = input(
            "Введите новый перевод на французский: ")
        dictionary[english_word] = new_french_translation
        print(f"Перевод слова '{english_word}' обновлен.")
    else:
        print(f"Слово '{english_word}' не найдено в словаре.")


def print_dictionary(dictionary):
    print("Словарь (английское слово - перевод на французский):")
    for english_word, french_translation in dictionary.items():
        print(f"{english_word} - {french_translation}")


english_french_dictionary = {}

while True:
    print("\nВыберите действие:")
    print("1. Добавить слово в словарь")
    print("2. Удалить слово из словаря")
    print("3. Найти перевод слова")
    print("4. Обновить перевод слова")
    print("5. Вывести весь словарь")
    print("6. Завершить программу")

    choice = input("Введите номер действия: ")

    if choice == '1':
        add_word(english_french_dictionary)
    elif choice == '2':
        remove_word(english_french_dictionary)
    elif choice == '3':
        search_word(english_french_dictionary)
    elif choice == '4':
        update_word(english_french_dictionary)
    elif choice == '5':
        print_dictionary(english_french_dictionary)
    elif choice == '6':
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите действие из списка.")


# Задание 3
def add_employee(company_dict):
    temp = {}
    name = input("Введите ФИО сотрудника: ")
    phone = input("Введите номер телефона: ")
    email = input("Введите email адрес: ")
    job_title = input("Введите должность: ")
    office_number = input("Введите номер кабинета: ")
    skype_nickname = input("Введите ник в Skype: ")

    temp["phone"] = phone
    temp["email"] = email
    temp["job_title"] = job_title
    temp["office_number"] = office_number
    temp["skype_nickname"] = skype_nickname

    company_dict[name] = temp
    return company_dict


def remove_employee(company_dict):
    del_name = input("Введите имя для удаления: ")
    if del_name in company_dict:
        print(f"Имя {del_name} удалено")
        del company_dict[del_name]
    else:
        print("Такого имени не существует!")
    return company_dict


def search_employee(company_dict):
    name_search = input("Введите имя для поиска: ")
    if name_search in company_dict:
        data = company_dict[name_search]
        print("Имя: ", name_search)
        print("Телефон: ", data["phone"])
        print("Email: ", data["email"])
        print("Должность: ", data["job_title"])
        print("Кабинет: ", data["office_number"])
        print("Skype: ", data["skype_nickname"])
    else:
        print("Такого имени нет в базе")
    return company_dict


def update_info(company_dict):
    name = input("Введите ФИО сотрудника для обновления данных: ")
    if name in company_dict:
        print("Выберите, что хотите обновить:")
        print("1. Номер телефона")
        print("2. Email")
        print("3. Должность")
        print("4. Номер кабинета")
        print("5. Ник в Skype")
        choice = input("Введите номер операции: ")

        if choice == "1":
            new_phone = input("Введите новый номер телефона: ")
            company_dict[name]["phone"] = new_phone
        elif choice == "2":
            new_email = input("Введите новый email адрес: ")
            company_dict[name]["email"] = new_email
        elif choice == "3":
            new_job_title = input("Введите новую должность: ")
            company_dict[name]["job_title"] = new_job_title
        elif choice == "4":
            new_office_number = input("Введите новый номер кабинета: ")
            company_dict[name]["office_number"] = new_office_number
        elif choice == "5":
            new_skype_nickname = input("Введите новый ник в Skype: ")
            company_dict[name]["skype_nickname"] = new_skype_nickname
        else:
            print("Некорректный выбор операции.")
    else:
        print("Такого имени нет в базе")
    return company_dict


temp_dict = {
    "Иванов Иван": {
        "phone": "123456789",
        "email": "ivanov@example.com",
        "job_title": "Менеджер",
        "office_number": "101",
        "skype_nickname": "ivan_ivanov"
    },
    "Петров Петр": {
        "phone": "987654321",
        "email": "petrov@example.com",
        "job_title": "Разработчик",
        "office_number": "202",
        "skype_nickname": "petr_petrov"
    }
}

while True:
    print("\nВыберите операцию:")
    print("1. Добавить сотрудника")
    print("2. Удалить сотрудника")
    print("3. Поиск сотрудника")
    print("4. Обновить информацию о сотруднике")
    print("5. Выйти")
    choice = input("Введите номер операции: ")

    if choice == "1":
        temp_dict = add_employee(temp_dict)
    elif choice == "2":
        temp_dict = remove_employee(temp_dict)
    elif choice == "3":
        temp_dict = search_employee(temp_dict)
    elif choice == "4":
        temp_dict = update_info(temp_dict)
    elif choice == "5":
        break
    else:
        print("Некорректный выбор операции. Пожалуйста, выберите снова.")


# Задание 4
def add_book(book_collection):
    book_info = {
        "author": input("Введите автора книги: "),
        "title": input("Введите название книги: "),
        "genre": input("Введите жанр книги: "),
        "year": input("Введите год выпуска книги: "),
        "pages": input("Введите количество страниц: "),
        "publisher": input("Введите издательство: ")
    }

    book_collection[book_info["title"]] = book_info
    return book_collection


def remove_book(book_collection):
    title = input("Введите название книги для удаления: ")
    if title in book_collection:
        print(f"Книга '{title}' удалена.")
        del book_collection[title]
    else:
        print("Книги с таким названием нет в коллекции.")
    return book_collection


def search_book(book_collection):
    title = input("Введите название книги для поиска: ")
    if title in book_collection:
        print("Информация о книге:")
        print("Автор:", book_collection[title]["author"])
        print("Жанр:", book_collection[title]["genre"])
        print("Год выпуска:", book_collection[title]["year"])
        print("Количество страниц:", book_collection[title]["pages"])
        print("Издательство:", book_collection[title]["publisher"])
    else:
        print("Книги с таким названием нет в коллекции.")


def update_book(book_collection):
    title = input("Введите название книги для обновления данных: ")
    if title in book_collection:
        print("Выберите, что хотите обновить:")
        print("1. Автор")
        print("2. Жанр")
        print("3. Год выпуска")
        print("4. Количество страниц")
        print("5. Издательство")
        choice2 = input("Введите номер операции: ")

        if choice2 == "1":
            new_author = input("Введите нового автора книги: ")
            book_collection[title]["author"] = new_author
        elif choice2 == "2":
            new_genre = input("Введите новый жанр книги: ")
            book_collection[title]["genre"] = new_genre
        elif choice2 == "3":
            new_year = input("Введите новый год выпуска книги: ")
            book_collection[title]["year"] = new_year
        elif choice2 == "4":
            new_pages = input("Введите новое количество страниц: ")
            book_collection[title]["pages"] = new_pages
        elif choice2 == "5":
            new_publisher = input("Введите новое издательство: ")
            book_collection[title]["publisher"] = new_publisher
        else:
            print("Некорректный выбор операции.")
    else:
        print("Книги с таким названием нет в коллекции.")
    return book_collection


book = {}

while True:
    print("\nВыберите операцию:")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Поиск книги")
    print("4. Обновить информацию о книге")
    print("5. Выйти")
    choice = input("Введите номер операции: ")

    if choice == "1":
        book = add_book(book)
    elif choice == "2":
        book = remove_book(book)
    elif choice == "3":
        search_book(book)
    elif choice == "4":
        book = update_book(book)
    elif choice == "5":
        break
    else:
        print("Некорректный выбор операции. Пожалуйста, выберите снова.")

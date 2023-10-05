# mtDict = {"key": 1, "ley2": 2, "key3": 3}
# myDict2 = {1: "one", 2: "two", 3: "three"}
#
# print(mtDict, "\n", myDict2)
#
# bookDict = {
#     "author": "author",
#     "title": "Python Course",
#     "price": 14.50,
#     "language": "English"
# }
#
# myDict3 = dict([("a", 1), ("b", 2)])
# print(myDict3)
#
# myDict4 = dict(["q1", "w2", "e3", "g4"])
# print(myDict4)
#
# myDict5 = dict(zip(["a", "b"], [1, 2]))
#
# print(myDict5)
#
# if "title" in bookDict:
#     print(bookDict["title"])
# else:
#     print("No data!")
#
# for elem in bookDict:
#     print(elem, bookDict[elem])
#
# bookDict["author"] = "Gvido"
# bookDict["pages"] = 350
#
# bookDict.update([("pages", 560), ("dicount", True)])
# del bookDict["title"]
#
#
# for key, value in bookDict.items():
#     print(key, value)
#
# print(bookDict.get("pages"))
# print(bookDict.pop("author"))
#
# print(bookDict.keys())
# print(list(bookDict.values()))
# print(bookDict.items())
#
#
# bookDict2 = bookDict.copy()
#
#


# users = [
#     {"name": "user1", "age": 20},
#     {"name": "user2", "age": 30},
#     {"name": "user3", "age": 40},
#     {"name": "user4", "age": 50},
# ]
#
# keyName = input("input info type: ")
# keyValue = input("input info value")
# keyValue = keyValue if keyName != "age" else int(keyValue)
#
# isFound = False
#
# for user in users:
#     if user.get(keyName) == keyValue:
#         print("Element is found!")
#         for key, val in user.items():
#             print(key, "-", val)
#         isFound = True
#         break
#
# if not isFound:
#     print("User not found!")


# film = {
#     "title": "Barbi",
#     "creator": "Daniel",
#     "rate": 8.2,
#     "year": [2022, 2023]
# }
#
# for key, value in film.items():
#     print(key, ": ", value)
#
# sortedFilm = sorted(film.items(), key=lambda x: x[0])
# print(sortedFilm)
#
# for elem in sortedFilm:
#     print(elem)
#
# film = dict(sortedFilm)
# print(film)
#
# keyList = list(film.keys())
# sortedKeys = sorted(keyList)
# for key in sortedKeys:
#     print(key, "=", film[key])


# users = [
#     {"name": "user1", "age": 20},
#     {"name": "user2", "age": 30},
#     {"name": "user3", "age": 40},
#     {"name": "user4", "age": 50},
# ]
#
# filtUser = list(filter(lambda user: user["age"] > 30, users))
# for i in filtUser:
#     for k, v in i.items():
#         print(k, v)

# Задание 1
def add_player(players):
    name = input("Введите имя баскетболиста: ")
    height = float(input("Введите рост (в см): "))
    players[name] = height
    print(f"Баскетболист добавлен.")
def remove_player(players):
    name = input("Введите имя которое нужно удалить: ")
    if name in players:
        del players[name]
        print(f"Баскетболист {name} удален.")
    else:
        print(f"Баскетболист не найден.")
def search_player(players):
    name = input("Введите имя для поиска: ")
    if name in players:
        print(f"Баскетболист {name} имеет рост {players[name]} см.")
    else:
        print(f"Баскетболист не найден.")
def update_player(players_dict):
    name = input("Введите имя баскетболиста: ")
    if name in players_dict:
        new_height = float(input("Введите новый рост баскетболиста: "))
        players_dict[name] = new_height
        print(f"Данные баскетболиста {name} обновлены")
    else:
        print(f"Баскетболист не найден.")

def print_players(players_dict):
    print("Информация о баскетболистах:")
    for name, height in players_dict.items():
        print(name, "-", height, "см")


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
        add_player(basketball_players)
    elif choice == '2':
        remove_player(basketball_players)
    elif choice == '3':
        search_player(basketball_players)
    elif choice == '4':
        update_player(basketball_players)
    elif choice == '5':
        print_players(basketball_players)
    elif choice == '6':
        break
    else:
        print("Некорректный выбор")


# Задание 1.1
def add_info(dict_data):
    key = input("Введите ключ: ")
    value = input("Введите значение ключа")
    dict_data[key] = value


def search(dict_data):
    key = input("Введите ключ для поиска: ")
    if key in dict_data:
        print(f"Значение ключа {key} = {dict_data[key]}")
    else:
        print("Ключе не найден")


myDict = {}

add_info(myDict)
search(myDict)


# Задание 2
def calculate_lengths(strings, result_dict):
    for string in strings:
        result_dict[string] = len(string)


myDict2 = {}
myList2 = ["dsff", "kexit", "dfsfdfsfdsdf"]

calculate_lengths(myList2, myDict2)
print(myDict2)

# Задание 3
myDict3 = {
    "aaa": 10,
    "bbb": 20,
    "ccc": 30
}


def filtersValue(filterDict, num):
    result = dict(filter(lambda item: item[1] > num, filterDict.items()))
    return result


print(filtersValue(myDict3, 10))

# Задание 4
myDict4 = {
    "aaa": 10,
    "bbb": 20,
    "ccc": 30
}


def deletedValues(myDict, value):
    new_dict = {k: v for k, v in myDict.items() if v >= value}
    return new_dict


print(deletedValues(myDict4, 30))


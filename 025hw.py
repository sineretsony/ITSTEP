import json
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
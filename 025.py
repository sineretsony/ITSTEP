import pickle
import json

# simpleObj = dict(int_list=[1, 2, 3, 4], text="test",
#                  number=4.4, none=None, boolean=True)

# with open('test.txt', 'wb') as file:
#     serialData = pickle.dumps(simpleObj)
#     print(serialData)
#     file.write(serialData)

# with open('test.txt', 'wb') as file:
#     pickle.dump(simpleObj, file)
#
# with open('test.txt', 'rb') as file:
#     decodObj = pickle.load(file)
#     print(decodObj)

#
# with open('test.json', 'w') as file:
#     json.dump(simpleObj, file, indent=4)
#
# with open('test.json', 'r') as file:
#     data = json.load(file)
#     print(data)

# import json
#
# musicObj = {
#     'Lana Del Rey': ['song1', 'song2', 'song3'],
#     'Hurts': ['song1', 'song222', 'song3'],
#     'Rey': ['song1', 'song2', 'song3']
# }
#
#
# def writeFile(fileName, obj):
#     fileName += '.json'
#     with open(fileName, 'w') as file:
#         data = json.dumps(obj, indent=4)
#         file.write(data)
#         print(data)
#
#
# def readFile(fileName):
#     fileName += '.json'
#     with open(fileName, 'r') as file:
#         data = json.loads(file.read())
#     return data
#
#
# def addInfo(fileName, group, nameSong):
#     dictFromFile = readFile(fileName)
#     if group in dictFromFile:
#         dictFromFile[group].append(nameSong)
#         writeFile(fileName, dictFromFile)
#
#
# def deleteInfo(group, fileName, nameSong="NoValue"):
#     dictFromFile = readFile(fileName)
#     if nameSong == "NoValue":
#         dictFromFile.pop(group)
#         writeFile(fileName, dictFromFile)
#     else:
#         valueForGroup = dictFromFile[group]
#         valueForGroup.remove(nameSong)
#         dictFromFile[group] = valueForGroup
#         writeFile(fileName, dictFromFile)
#
#
# def findInfo(file, group=None, nameSong=None):
#     dictFromFile = readFile(file)
#     if group in dictFromFile.keys() and nameSong is None:
#         return f'Grops name is {group} \n Songs: {dictFromFile[group]}'
#     elif nameSong is not None and group is None:
#         for k, v in dictFromFile.items():
#             if nameSong in v:
#                 return k, v
#
#
# writeFile('test', musicObj)
# addInfo('test', 'Lana Del Rey', 'song5')
# deleteInfo('Lana Del Rey', 'test', nameSong="song1")
#
# print(readFile('test'))
# print(findInfo('test', nameSong='song2'))


# # Задание 1
#
# countries_capitals = {
#     'Украина': 'Киев',
#     'США': 'Вашингтон',
#     'Франция': 'Париж'
# }
#
#
# def addInfo(dict_data, new_country, capital):
#     if new_country not in dict_data:
#         dict_data[new_country] = capital
#     else:
#         print(f"Странa {new_country} уже есть в словаре.")
#     return dict_data
#
#
# def delInfo(dict_data, del_country):
#     if del_country in dict_data:
#         del dict_data[del_country]
#     else:
#         print(f"Страны {del_country} нет в словаре.")
#     return dict_data
#
#
# def searchInfo(dict_data, search_country):
#     if search_country in dict_data:
#         return dict_data[search_country]
#     else:
#         return "Страна не найдена."
#
#
# def editInfo(dict_data, country, new_capital):
#     if country in dict_data:
#         dict_data[country] = new_capital
#     else:
#         print(f"Страны {country} нет в словаре.")
#     return dict_data
#
#
# def saveInfo(dict_data, filename):
#     filename += '.json'
#     with open(filename, 'w', encoding='utf-8') as file:
#         json.dump(dict_data, file)
#
#
# def loadInfo(filename):
#     with open(filename, 'r') as file:
#         dict_data = json.load(file)
#     return dict_data
#
#
# print(countries_capitals)
# print(addInfo(countries_capitals, 'Украина', 'Гданск'))
# print(delInfo(countries_capitals, 'США'))
# print(searchInfo(countries_capitals, 'Польша'))
# print(editInfo(countries_capitals, 'Польша', 'Варшава'))
# saveInfo(countries_capitals, 'test2')
# print(loadInfo('test2'))


# Задание 2

import json


def dataMerge():
    tempData = {}

    while True:
        inputNameFile = input("Введите название файла: ")

        if inputNameFile == 'quit':
            with open('data_merge.json', 'w', encoding='utf-8') as file:
                json.dump(tempData, file, indent=4)
                print("Информация была сохранена в файл: data_merge.json")
            break

        try:
            with open(inputNameFile, 'r', encoding='utf-8') as file:
                tempData[inputNameFile] = file.read()
        except FileNotFoundError:
            print(f"Файл {inputNameFile} не найден.")
        except:
            print(f"Произошла ошибка при чтении файла {inputNameFile}")


dataMerge()


# def dataMerge2():
#     tempData = []
#
#     while True:
#         inputNameFile = input("Введите название файла: ")
#
#         if inputNameFile == 'quit':
#             with open('data_merge.json', 'a', encoding='utf-8') as file:
#                 for file_data in tempData:
#                     file.write(f'{file_data[0]}: {file_data[1]}\n')
#                 print("Информация была сохранена в файл: data_merge.json")
#             break
#
#         try:
#             with open(inputNameFile, 'r', encoding='utf-8') as file:
#                 file_data = (inputNameFile, file.read())
#                 tempData.append(file_data)
#         except FileNotFoundError:
#             print(f"Файл {inputNameFile} не найден.")
#         except:
#             print(f"Произошла ошибка при чтении файла {inputNameFile}")
#
#
# dataMerge()


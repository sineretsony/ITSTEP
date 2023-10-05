# emptyTuple = ()
# emptyTuple2 = tuple()
#
# myTuple = (1, 2, 3, "txt", False)
# myTuple2 = (1,)
#
# print(myTuple[2])
#
# myTuple3 = tuple(("aga", "da"))
#
# print(len(myTuple3))
#
# del myTuple3
#

# user = ("1", "2", "3")
# a, b, c = user
#
# user = ("1", "2", "3")
# k, *v = user
#
#
# def ask():
#     hobbyList = []
#     while True:
#         hobbyName = input("Введите хобби: ")
#         if hobbyName == "":
#             print("End")
#             break
#         else:
#             hobbyList.append(hobbyName)
#     return hobbyList
#
#
# myHobby = tuple(ask())
# print(myHobby)

# # Задание 1
# fruits_tuple = (
#     'яблоко', 'груша', 'банан', 'апельсин', 'яблоко', 'ананас', 'яблоко',
#     'груша')
#
# fruit_input = input('Введите название фрукта: ').lower()
#
# fruit_count = fruits_tuple.count(fruit_input)
#
# if fruit_count > 0:
#     print(f'Фрукт {fruit_input} встречается {fruit_count} раз(а).')
# else:
#     print(f'Фрукт {fruit_input} не найден.')
#
#
# # Задание 2
# def calc_items(items_list):
#     total_items = 0
#
#     for i in items_list:
#         total_items += i[1]
#
#     return total_items
#
#
# input_data = [('Яблоки', 10), ('Молоко', 5), ('Хлеб', 3), ('Масло', 2)]
#
# items_count = calc_items(input_data)
# print('Общее количество товаров:', items_count)

# # Задание 3
# from functools import reduce
#
#
# def sort(input_list):
#     sorted_list = reduce(
#         lambda acc, item: acc + [item] if not acc or acc[-1][1] <= item[
#             1] else [item] + acc, input_list, [])
#     return sorted_list
#
#
# input_data = [("Андрей", 5000), ("Марина", 3000), ("Иван", 8000),
#               ("Елена", 6000)]
# sorted_salary = sort(input_data)
#
# reduce(lambda x, item: print(f'{item[0]}: {item[1]}'), sorted_salary, None)
#
# # Задание 4
#
# input_data2 = [("Анна", 22), ("Иван", 16), ("Мария", 20), ("Петр", 25)]
#
# filter_name = filter(lambda x: x[1] > 18, input_data2)
# filter_name = [item[0] for item in filter_name]
# result = ' '.join(filter_name)
#
# print(result)
#
#
# # Задание 5
# def calc_dist(point1, point2):
#     x1, y1 = point1
#     x2, y2 = point2
#     dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#     return dist
#
#
# point1 = (3, 4)
# point2 = (6, 8)
#
# dist = calc_dist(point1, point2)
#
# print(f"Расстояние между точками {point1} и {point2} составляет: {dist}")


# mySet1 = {1, 2, 3}
#
# mySet2 = {"stud1", "stud2"}
#
# mySet3 = {23, "styd1", False, (12, 23), "styd2"}
#
# print(type(mySet3))
# print(mySet3)
#
# mySet4 = set((10, 20, 30))
# print(mySet4)
#
# listUsers = ["user1", "user1", "user2", "user3"]
# uniqueList = set(listUsers)
# print(list(uniqueList))
#
# mySeta = {1, 2, 3}
# mySetb = {3, 2, 1}
#
# print(mySeta == mySetb)
#
# for i in uniqueList:
#     print(i)


# mySeta = {1, 2, 3}
# print(mySeta)
# mySeta.add(5)
# print(mySeta)
# mySeta.update([8, 9, 6, 5])
# print(mySeta)
# mySeta.discard(8)
# print(mySeta)
# mySeta.remove(6) #raise
# print(mySeta)
# mySeta.clear()
# print(mySeta)
#

# productList1 = {"iphone10", "iphone11", "iphone12", "iphone13"}
# productList2 = {"iphone12", "iphone13", "iphone14", "iphone15"}
#
# print("list 1", productList1)
# print("list 2", productList2)
#
# print("intersection &", productList1 & productList2)
# print("intersection &", productList1.intersection(productList2))
#
# print("union |", productList1 | productList2)
# print("union |", productList1.union(productList2))
#
# print("difference", productList1 - productList2)
# print("difference", productList2 - productList1)
# print("difference", productList1.difference(productList2))
#
# print(sorted(productList1))
#

# # Задание 1
# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a | b)
#
# # Задание 2
# print(a.intersection(b))
#
# # Задание 3
# print(a.difference(b))
#
# # Задание 4
# data = [('Иванов Иван Иванович', 22, 'Группа 1'),
#         ('Петров Петр Петрович', 20, 'Группа 2'),
#         ('Сидорова Екатерина Александровна', 21, 'Группа 1'),
#         ('Смирнов Алексей Иванович', 23, 'Группа 2')]
#
# groups = set(i[2] for i in data)
#
# print("Список групп:", ' '.join(sorted(groups)))

# Задание 5
text = ("Python - отличный язык программирования. "
        "Множества в Python позволяют выполнять уникальные операции. "
        "Язык Python популярен и прост в изучении.")

text = (text.replace('.', '').replace(',', '')
        .replace('-', '').replace(':', '')
        .replace(';', '').replace('!', '')
        .replace('?', ''))

uws = set(text.lower().split())

print("Список уникальных слов в тексте:")
print(uws)

ui = input("Введите слово для проверки: ").lower()
if ui in uws:
    print(f"Слово '{ui}' есть в тексте.")
else:
    print(f"Слова '{ui}' нет в тексте.")

uw = input("Введите слова через пробел для множества 2: ").lower().split()

uws_user = set(uw)

i = uws.intersection(uws_user)
un = uws.union(uws_user)
diff = uws.difference(uws_user)

i_count = len(i)
dif_count = len(diff)

print("Пересечение множеств (слова, встречающиеся в обоих множествах):", i)
print("Объединение множеств:", un)
print("Разность множеств (слова, встречающиеся только в первом множестве):",
      diff)
print(f"\nКоличество слов в пересечении: {i_count}")
print(f"Количество слов в разности: {dif_count}")

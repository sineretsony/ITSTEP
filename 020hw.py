from random import randint as random

# Задание 1

list_num = [random(-100, 100) for i in range(20)]

print(list_num)
print("Только положителные числа: ", list(filter(lambda x: x >= 0, list_num)))

# Задание 2
list_num2 = [random(-10000, 10000) for x in range(20)]


def filers_num(a, b, lst):
    return a <= lst <= b


temp = input("Введите диапазон от и до через пробел: ")
temp2 = temp.split(" ")

print("Числа в диапазоне: ", list(filter(
    lambda x: filers_num(int(temp2[0]), int(temp2[1]), x), list_num2)))

# Задание 3
list_num3 = [1, 2.3, 5, 7, 7.3, 7.7]

print("Только целочисленные",
      list(filter(lambda it: isinstance(it, int), list_num3)))

# Задание 4
users_login = ["Gava", "Maga", "Pip", "Digo"]


def modyf_login(log):
    return log + "$"


print("Новые логины с приставкой $ ", list(map(modyf_login, users_login)))

# Задание 5
list_num4 = [1, 2, 3, 4, 5]
list_num5 = [1, 7, 3, 4, 5]
list_num6 = [1, 2, 7, 4, 9]


def three_list_filter(a, b, c):
    temp = []
    for i in a:
        if i in b and i in c:
            temp.append(i)
    return temp


print((three_list_filter(list_num4, list_num5, list_num6)))

# Задание 6
list_num7 = [random(-100, 100) for h in range(10)]

print("Числа преобразованные в строки: ", list(map(lambda x: str(x), list_num7)))

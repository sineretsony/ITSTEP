# from random import randint as random
# from math import inf
# from functools import reduce
#
# # Задание 1 классная
# lst = [(lambda i: i * 2)(i) for i in range(1, 5)]
# print(lst)
#
# # Задание 2 классная
# '''не совсем моё исполнение лямбда рекурсии, это взрыв мозга,
# примерное понимаю что тут происходит,
# но уверен такой вариант решения мне никогда не пригодится.
# Это чтобы не использовать map'''
#
# input_str = input("Введите список чисел, через пробел: ")
# numbers = [float(x) for x in input_str.split()]
#
# max_value = (lambda f: lambda lst, idx, mv: mv if idx == len(lst)
# else f(f)(lst, idx + 1, lst[idx]) if lst[idx] > mv
# else f(f)(lst, idx + 1, mv))(
#     lambda f: lambda lst, idx, mv: mv if idx == len(lst)
#     else f(f)(lst, idx + 1, lst[idx]) if lst[idx] > mv
#     else f(f)(lst, idx + 1, mv))(numbers, 0, -inf)
#
# min_value = (lambda f: lambda lst, idx, mv: mv if idx == len(lst)
# else f(f)(lst, idx + 1, lst[idx]) if lst[idx] < mv
# else f(f)(lst, idx + 1, mv))(lambda f: lambda lst, idx, mv: mv
# if idx == len(lst) else f(f)(lst, idx + 1, lst[idx])
# if lst[idx] < mv else f(f)(lst, idx + 1, mv))(numbers, 0, inf)
#
# print(f"Максимальное значение {max_value}")
# print(f"Минимальное значение {min_value}")
#
# # --------------------------------------------------------------------------
# # Задание 1
#
# str1 = "What is lost, will be found"
# result = (lambda x: x.replace(" ", "_"))(str1)
# print(result)
#
# # Задание 2
#
# lst1 = [random(1, 100) for i in range(10)]
#
# print(lst1)
# print("Сумма всех числе в списке: ", reduce(lambda x, t=0: t + x, lst1))
# print("Среднее арифм. всех чисел: ",
#       reduce(lambda x, y: x + y, lst1) / len(lst1))
#
# # Задание 3
#
# list_a = ["a", "b", True, 5]
# list_b = ["g", False, 0, 56]
#
#
# def unifier(a, b):
#     return a + b
#
#
# print(unifier(list_a, list_b))
# result2 = (lambda a, b: a + b)
# print(result2(list_a, list_b))
#
#
# # Задание 4
#
# def common_divisor(a, b):
#     if b == 0:
#         return a
#     else:
#         return common_divisor(b, a % b)
#
#
# print(common_divisor(68, 24))
#
#
# # Задание 5 доп
# def random_secret_num():
#     secret_num = [random(1, 9) for i in range(4)]
#     return secret_num
#
#
# def search_num_index(x, s):
#     count = 0
#     for o, tw in zip(x, str(s)):
#         if o == int(tw):
#             count += 1
#     return count
#
#
# def in_nums(s, x, index=0):
#     if index == len(s):
#         return 0
#     else:
#         last_digit = s[index]
#         count = (str(last_digit) in str(x)) + in_nums(s, x, index + 1)
#         return count
#
#
# def games():
#     secrets_num = random_secret_num()
#     count_input = 1
#
#     while True:
#         print("Секретный код сгенерирован, 4 цифры от 1 до 9")
#         print(secrets_num)  # для поверки
#         input_secret_num = input("Попробуйте угадать код: ")
#         print("Цифр угадано", in_nums(secrets_num, input_secret_num))
#         print("Цифр угадано и стоит на нужном месте",
#               search_num_index(secrets_num, input_secret_num))
#
#         if search_num_index(secrets_num, input_secret_num) == 4:
#             print(
#                 f"Вы отличнj спарвились, угадали все цифры за {count_input} попиток")
#             break
#         count_input += 1
#
#
# games()


# Доп от себя
def cashFunc(func):
    cashDict = []

    def outWrapper(*args, **kwargs):
        print(cashDict)
        key = (args, frozenset(kwargs.items()))

        for item in cashDict:
            if item[0] == key:
                print("Результат получен из кэша")
                return item[1]

        result = func(*args, **kwargs)
        cache_entry = (key, result)
        cashDict.append(cache_entry)
        print("Результат сохранён в кэш")

        if len(cashDict) > 4:
            cashDict.pop(0)

        return result

    return outWrapper


@cashFunc
def uppInter(x):
    temp = 0
    for i in range(x):
        temp = i * x
    return temp


print(uppInter(67))
print(uppInter(667))
print(uppInter(67))
print(uppInter(679))



matrix = [[1, "s", 3],
          [4, 5, "g"],
          ["h", 8, 9]]

matrix2 = [[1, "z", 3],
          [4, 5, "g"],
          ["h", 8, 9]]

matrix3 = [[1, "s", 3],
          [4, 7, "g"],
          ["h", 8, 9]]




@cashFunc
def transpose(t):
    try:
        elements_list = sum(t, [])
    except TypeError:
        print("Ошибка, у вас не вложенный список")
        return None

    width, height = len(t[0]), len(t)

    def map_index(n, k, m=1):
        if m == n + 1:
            return []
        else:
            x = [y for y in reversed(range(m, n * k + 1, n))]
            # print(x)
            return x + map_index(n, k, m + 1)

    link_ind = map_index(width, height)

    def add_results(n):
        results, temp = [], []
        for i in n:
            temp.append(elements_list[i - 1])
            if len(temp) == len(t):
                results.append(temp)
                temp = []
        return results

    matrix_rotation = add_results(link_ind)
    return matrix_rotation


print(transpose(matrix))
print(transpose(matrix))
print(transpose(matrix2))
print(transpose(matrix3))

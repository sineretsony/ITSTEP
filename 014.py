# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# operator = input("Введите оператор (+, -, /, *, mod, pow, div): ")
#
# result = 0
#
# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
# elif operator == "/":
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         print("Ошибка: деление на ноль")
# elif operator == "mod":
#     if num2 != 0:
#         result = num1 % num2
#     else:
#         print("Ошибка: деление на ноль")
# elif operator == "pow":
#     result = num1 ** num2
# elif operator == "div":
#     if num2 != 0:
#         result = num1 // num2
#     else:
#         print("Ошибка: деление на ноль")
# else:
#     print("Неподдерживаемая операция")
#
# print("Результат:", result)

count = 0

# while count < 10:
#     count += 1
#     print(count)
# else:
#     print(333)
#

# while True:
#     num = int(input("Введите число: "))
#     if num < 0:
#         continue
#     elif num == 0:
#         break
#     print(num)

# fuel = 50
# distance = 50
# km = 0
# while distance > 0 <= fuel:
#     print("Остаток km", distance)
#     print(f"{fuel}%")
#     if fuel >= 30:
#         fuel -= 30
#     else:
#         print("Нет топлива")
#         gas = int(input("Заправка: "))
#         fuel += gas
#         if gas == 0:
#             break
#     distance -= 10
#     while km < 10:
#         km += 1
#     km = 0
# else:
#     print(f"Finish топливо {fuel} остаток км {distance}")

# start = 0
# end = 100
# sum = 0
# i = 0
#
# while start < end:
#     sum += start
#     i += 1
#     start += 1
# print("Sum", sum)
# print("i ", i)
# print("avg", sum / i)

# import random
# from random import randint
#
# ran = randint(1, 10)
# print(ran)

# # Задача 1
# num1 = int(input("Введите число 1 "))
# num2 = int(input("Введите число 2 "))
#
# if num1 > num2:
#     temp = num1
#     num1 = num2
#     num2 = temp
#
# while num1 <= num2:
#     print(num1)
#     num1 += 1
#
# # Задача 2
# num3 = int(input("Введите число 1: "))
# num4 = int(input("Введите число 2: "))
#
# if num3 > num4:
#     temp = num3
#     num3 = num4
#     num4 = temp
#
# if num3 % 2 == 0:
#     num3 += 1
#
# while num3 <= num4:
#     print(num3)
#     num3 += 2
#
# # Задача 3
# num5 = int(input("Введите число 1: "))
# num6 = int(input("Введите число 2: "))
#
# if num5 > num6:
#     temp = num5
#     num5 = num6
#     num6 = temp
#
# if num5 % 2 != 0:
#     num5 += 1
#
# while num5 <= num6:
#     print(num5)
#     num5 += 2
#
# # Задача 4
# num7 = int(input("Введите число 1: "))
# num8 = int(input("Введите число 2: "))
#
# if num7 < num8:
#     temp = num7
#     num7 = num8
#     num8 = temp
#
# while num7 >= num8:
#     print(num7)
#     num7 -= 1
#
# # Задача 5
# num9 = int(input("Введите число 1: "))
# num10 = int(input("Введите число 2: "))
#
# if num9 > num10:
#     temp = num9
#     num9 = num10
#     num10 = temp
#
# if num9 % 2 == 0:
#     num9 += 1
#
# while num9 <= num10:
#     print(num9)
#     num9 += 2
#
#
#
# # Задача 6
# length1 = int(input("Введите длину линии: "))
# line = '*' * length1
# print(line)
#
# # Задача 7
# length2 = int(input("Введите длину линии: "))
# symbol = input("Введите символ для заполнения: ")
# line = symbol * length2
# print(line)
#
# # Задача 8
# width = int(input("Введите ширину фигуры: "))
# height = int(input("Введите высоту фигуры: "))
#
# i = 0
# while i < height:
#     print(' * ' * width)
#     i += 1
#
# # Задача 8.2
# width2 = int(input("Введите ширину фигуры: "))
# height2 = int(input("Введите высоту фигуры: "))
#
# i = 0
# while i < height2:
#     if i == 0 or i + 1 == height2:
#         print(' * ' * width2)
#     else:
#         print(' * ' + ("   " * (width2 - 2)) + ' * ')
#     i += 1

while True:
    print("Программа конвертера валют")
    print("1. Доллары в Евро")
    print("2. Евро в Доллары")
    print("3. Выход")
    print("------------------------")
    choice = int(input("Выберите операцию (1/2): "))
    print("------------------------")

    if choice == 1:
        usd = float(input("Введите сумму $: "))
        eur = usd * 0.85
        print(f"{usd} долларов = {eur} евро")
    elif choice == 2:
        eur = float(input("Введите сумму в евро: "))
        usd_res = eur / 0.85
        print(f"{eur} евро = {usd_res} долларов")
    elif choice == 3:
        break
    else:
        print("Неверный выбор.")
        continue


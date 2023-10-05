import random
import string

# try:
#     amount = int(input("Enter the amount if new irems - "))
#     items_type = input("Enter the type if item - ")
#     parts_number = int(input("Enter the number parts - "))
#     parts = amount / parts_number
# except ValueError:
#     print("Amount shoiled be an integer!")
# except ZeroDivisionError:
#     print("Cant's devide!")
# finally:
#     print("The program is over!")

# try:
#     raise ValueError("truble 1")
# except BaseException as ex:
#     print(type(ex).__name__)
#     print(ex)
#     print("323")

# # Задание 1
# user_num = 0
#
# try:
#     user_num = int(input("Введите число: "))
# except ValueError as ex:
#     print(f"Произошла ошибка, введите число!\n"
#           f"Ошибка: {ex}")
# except:
#     print("Произошла другая ошибка, попробуйте еще раз")
#
# if user_num % 2 == 0:
#     print("Even number")
# elif user_num % 2 != 0:
#     print("Odd number")
#
# # Задание 2
# try:
#     user_input = int(input("Введите число: "))
#
#     if user_input < 0:
#         raise ValueError("Только для положительных целых чисел")
#
#     factorial = 1
#     count = 1
#     while count <= user_input:
#         factorial *= count
#         count += 1
#
#     print(f"Факториал числа {user_input} равен {factorial}")
# except ValueError as ve:
#     print("Произошла ошибка, введите положительное число!")
#     print(ve)
# except:
#     print("Произошла другая ошибка, попробуйте еще раз")

# Задание 3
# balance = 200
# fil = True
#
# while True:
#     if fil:
#         print("Пополнить банковскую карту (1)\n"
#               "Снять наличные          (2)\n"
#               "Завершить работу        (3)")
#         fil = False
#
#     user_command = input("Введите действие: ")
#
#     try:
#         if user_command == "1":
#             print("На счету", balance)
#             amount = int(input("Введите сумму: "))
#             balance += amount
#             print("На счету", balance)
#
#         elif user_command == "2":
#             print("На счету", balance)
#             amount = int(input("Введите сумму: "))
#             if balance - amount < 0:
#                 raise ValueError("Недостаточно средств на счету")
#             balance -= amount
#             print("На счету", balance)
#
#         elif user_command == "3":
#             break
#         else:
#             print("Неверная команда. Пожалуйста, выберите 1, 2 или 3.")
#
#     except ValueError as e:
#         print("Ошибка, введите сумму:", e)
#     except:
#         print("Произошла другая ошибка, попробуйте еще раз")

# # Задание 4
#
# try:
#     password = int(input("Введите желаемую длину пароля: "))
#     rand_pass = ""
#     base = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a', 'B',
#             'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h',
#             'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O',
#             'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u',
#             'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
#
#     if password <= 0:
#         print("Длина пароля должна быть положительным числом.")
#     else:
#         while password >= 0:
#             password -= 1
#             i = random.randint(1, len(base) -1)
#             rand_pass += base[i]
#
#         print("Сгенерированный пароль:", rand_pass)
#
# except ValueError:
#     print("Пожалуйста, введите корректное число.")
# except:
#     print("Произошла ошибка, попробуйте еще раз")
#
#
# # Задание 5
#
# correct = 0
# tot_quest = 5
# ques_count = 0
#
# print("Давайте тренироваться в умножении!")
#
# while ques_count < tot_quest:
#     num1 = random.randint(1, 10)
#     num2 = random.randint(1, 10)
#     result = num1 * num2
#
#     try:
#         user_answer = int(input(f"Сколько будет {num1} умножить на {num2}? "))
#
#         if user_answer == result:
#             print("Правильно! Молодец!")
#             correct += 1
#         else:
#             print(f"Неправильно. Правильный ответ: {result}")
#
#         ques_count += 1
#
#     except ValueError:
#         print("Пожалуйста, введите корректное число.")
#     except:
#         print("Произошла другая ошибка, попробуйте еще раз")
#
# print(
#     f"Тренировка завершена. Вы правильно ответили на {correct} из {tot_quest} вопросов.")




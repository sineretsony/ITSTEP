# Задача 1

num1 = 0
num2 = 0
count = 1

while count == 1 or num1 <= num2 or count == 2:
    if count == 1:
        num1 = int(input("Введите начало диапазона: "))
        count += 1
        continue
    elif count == 2:
        num2 = int(input("Введите конец диапазона: "))
        count += 1
        continue
    num1 += 1
    count += 1
    if num1 % 7 == 0:
        print(f"Число кратно {num1} кратно 7")
else:
    print("Конец диапазона")

# Задача 2

num3 = 0
num4 = 0
count2 = 1
numbers1 = ""
numbers2 = ""
multiple_7 = ""
multiple_5 = ""

while count2 == 1 or num3 <= num4 or count2 == 2:
    if count2 == 1:
        num3 = int(input("Введите начало диапазона: "))
        count2 += 1
        continue
    elif count2 == 2:
        num4 = int(input("Введите конец диапазона: "))
        count2 += 1
        continue
    numbers1 += str(num3) + ": "
    temp1 = numbers2
    numbers2 = str(num3) + ": "
    numbers2 += temp1
    temp1 = ""
    if num3 % 7 == 0:
        multiple_7 += str(num3) + ": "
    if num3 % 5 == 0:
        multiple_5 += str(num3) + ": "

    num3 += 1
    count2 += 1

else:
    print("Конец диапазона")
print(f"Числа диапазона {numbers1}")
print(f"Числа реверс ди {numbers2}")
print(f"Числа кратные семи: {multiple_7}")
print(f"Числа кратные пяти: {multiple_5}")

# Задача 3

num5 = 0
num6 = 0
count3 = 1
even_sum = 0
odd_sum = 0
multiple_9_sum = 0
even_count = 0
odd_count = 0
multiple_9_count = 0

while count3 == 1 or num5 <= num6 or count3 == 2:
    if count3 == 1:
        num5 = int(input("Введите начало диапазона: "))
        count3 += 1
        continue
    elif count3 == 2:
        num6 = int(input("Введите конец диапазона: "))
        count3 += 1
        continue

    if num5 % 2 == 0:
        even_sum += num5
        even_count += 1
    else:
        odd_sum += num5
        odd_count += 1

    if num5 % 9 == 0:
        multiple_9_sum += num5
        multiple_9_count += 1

    num5 += 1
    count3 += 1

print("Конец диапазона")

if even_count > 0:
    even_average = even_sum / even_count
else:
    even_average = 0

if odd_count > 0:
    odd_average = odd_sum / odd_count
else:
    odd_average = 0

if multiple_9_count > 0:
    multiple_9_average = multiple_9_sum / multiple_9_count
else:
    multiple_9_average = 0

print(f"Сумма четных чисел: {even_sum}")
print(f"Сумма нечетных чисел: {odd_sum}")
print(f"Сумма чисел, кратных 9: {multiple_9_sum}")
print(f"Среднее арифметическое четных чисел: {even_average}")
print(f"Среднее арифметическое нечетных чисел: {odd_average}")
print(f"Среднее арифметическое чисел, кратных 9: {multiple_9_average}")

# Задача 4

len_line = int(input("Введите длину линии: "))
line_symbol = input("Введите символ линии: ")

line = ""
while len_line != 0:
    line += line_symbol + "\n"
    len_line -= 1
print(line)

# Задача 5

while True:
    number = float(input("Введите число: "))

    if number == 7:
        print("Good bye!")
        break
    elif number < 0:
        print("Number is negative")
    elif number == 0:
        print("Number is equal to zero")
    elif number > 0:
        print("Number is positive")

# Задача 6

sum_of_num = 0
maxi_num = 0
min_num = 0


while True:
    number2 = float(input("Введите число: "))

    if number2 == 7:
        print("Good bye!")
        break
    sum_of_num += number2
    if maxi_num == 0:
        maxi_num = number2
    elif number2 > maxi_num:
        maxi_num = number2
    if min_num == 0:
        min_num = number2
    elif number2 < min_num:
        min_num = number2

print(f"Сумма введённых числе - {sum_of_num}\n"
      f"Максимальное число - {maxi_num}\n"
      f"Минимальное число - {min_num}\n")


"""И так, меня что-то понесло, и 7-я задача... это "жесть")
Поэтому я оставлю здесь первый вариант решения без лишних частей кода
---------------------------------------------------------------------"""

# Задача 7 (не жесть)
# count_numbers = 0
# sum_numbers = 0
# average = 0
# zero_users = 0
#
#
# print("Добро пожаловать!\n"
#       "----------------------------------------\n"
#       "Для подсчёта суммы всех цифр в числе (A)\n"
#       "Для подсчёта кол-ва цифр в числе_____(B)\n"
#       "Для подсчёта нулей___________________(C)\n"
#       "Ввести новое число________________(N)(1)\n"
#       "Выход из программы________________(X)(0)\n"
#       "----------------------------------------")
#
# user_input = input("Введите число: ")
#
# while True:
#     user_action = input("Введите действие (A, B, C, N-1, X-0: ")
#
#     if user_action == "N" or user_action == "1":
#         user_input = input("Введите новое число: ")
#         count_numbers = 0
#         sum_numbers = 0
#         average = 0
#         zero_users = 0
#         continue
#
#     if user_action == "X" or user_action == "0":
#         break
#     for i in user_input:
#         if user_action == "A":
#             sum_numbers += int(i)
#         elif user_action == "B":
#             count_numbers += 1
#         elif user_action == "C":
#             if i == "0":
#                 zero_users += 1
#     if user_action == "A":
#         print("Сумма всех цифр: ", sum_numbers)
#     elif user_action == "B":
#         print("Цифр в числе: ", count_numbers)
#     elif user_action == "C":
#         if zero_users == 0:
#             print("Нулей в числе нет")
#         else:
#             print("Нулей в числе: ", zero_users)


# Задача 7 (тут жесть)

count_numbers = 0
sum_numbers = 0
average = 0
zero_users = 0

user_input = ""
user_action = ""
filters = False

# settings
letter_sum_numbers = "A"
letter_count_numbers = "B"
letter_zero_users = "C"
letter_average = "D"
letter_settings = "F"
settings_status = False

while True:
    if not settings_status:
        print(f"Добро пожаловать!\n"
              "----------------------------------------\n"
              f"Для подсчёта суммы всех цифр в числе ({letter_sum_numbers})\n"
              f"Для подсчёта кол-ва цифр в числе_____({letter_count_numbers})\n"
              f"Для подсчёта нулей___________________({letter_zero_users})\n"
              f"Для подсчёта среднее арифметического_({letter_average})\n"
              f"Ввести новое число________________(N)\n"
              f"Настройки_________________________({letter_settings})\n"
              f"Выход из программы________________(X)(0)\n"
              "----------------------------------------")
        settings_status = True

    if not filters:
        user_action = input(f"Введите действие ({letter_sum_numbers}, "
                            f"{letter_count_numbers}, {letter_zero_users}, "
                            f"{letter_average}, N-1, {letter_settings}, X-0: ")

    if user_action == "X" or user_action == "0":
        print("Good bye!")
        break

    if user_input == "" and user_action != letter_settings:
        user_action = "N"

    if user_action == "N" or user_action == "1" and filters:
        user_input = input("Введите число: ")
        for j in user_input:
            if j not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                print("Неверный ввод")
                user_input = ""
                break

        count_numbers = 0
        sum_numbers = 0
        average = 0
        zero_users = 0
        filters = False
        continue

    for i in user_input:
        if user_action == letter_sum_numbers:
            sum_numbers += int(i)
            count_numbers += 1
        elif user_action == letter_count_numbers:
            count_numbers += 1
        elif user_action == letter_zero_users:
            if i == "0":
                zero_users += 1
            count_numbers += 1
        elif user_action == letter_average:
            count_numbers += 1
            sum_numbers += int(i)

    if user_action == letter_sum_numbers:
        print("Сумма всех цифр: ", sum_numbers)
    elif user_action == letter_count_numbers:
        print("Цифр в числе: ", count_numbers)
    elif user_action == letter_zero_users:
        if zero_users == 0:
            print("Нулей в числе нет")
        else:
            print("Нулей в числе: ", zero_users)
    elif user_action == letter_average:
        average = sum_numbers / count_numbers
        print("Среднее арифметическое:", average)

    if user_action == "F":
        while True:
            if settings_status:
                print(f"---------------Настройки---------------\n"
                      "----------------------------------------\n"
                      f"Для подсчёта суммы всех цифр в числе ({letter_sum_numbers})\n"
                      f"Для подсчёта кол-ва цифр в числе_____({letter_count_numbers})\n"
                      f"Для подсчёта нулей___________________({letter_zero_users})\n"
                      f"Для подсчёта среднее арифметического_({letter_average})\n"
                      f"Настройки_________________________({letter_settings})\n"
                      "----------------------------------------\n"
                      f"Выход без сохранения Y выход с новыми настроками S)\n"
                      f"Введите символ пункта настройки")
                settings_status = False

            new_settings = input("Символ для выбора настройки: ")

            if new_settings == letter_sum_numbers:
                temp2 = letter_sum_numbers
                letter_sum_numbers = input("Введите новый символ: ")
                if (letter_sum_numbers == letter_count_numbers
                        or letter_sum_numbers == letter_zero_users
                        or letter_sum_numbers == letter_average
                        or letter_sum_numbers == letter_settings):
                    letter_sum_numbers = temp2
                    temp2 = ""
                    print("Данный символ сейчас недоступен")
            elif new_settings == letter_count_numbers:
                temp2 = letter_count_numbers
                letter_count_numbers = input("Введите новый символ: ")
                if (letter_count_numbers == letter_sum_numbers
                        or letter_count_numbers == letter_zero_users
                        or letter_count_numbers == letter_average
                        or letter_count_numbers == letter_settings):
                    letter_count_numbers = temp2
                    temp2 = ""
                    print("Данный символ сейчас недоступен")
            elif new_settings == letter_zero_users:
                temp2 = letter_zero_users
                letter_zero_users = input("Введите новый символ: ")
                if (letter_zero_users == letter_sum_numbers
                        or letter_zero_users == letter_count_numbers
                        or letter_zero_users == letter_average
                        or letter_zero_users == letter_settings):
                    letter_zero_users = temp2
                    temp2 = ""
                    print("Данный символ сейчас недоступен")
            elif new_settings == letter_average:
                temp2 = letter_average
                letter_average = input("Введите новый символ: ")
                if (letter_average == letter_sum_numbers
                        or letter_average == letter_count_numbers
                        or letter_average == letter_zero_users
                        or letter_average == letter_settings):
                    letter_average = temp2
                    temp2 = ""
                    print("Данный символ сейчас недоступен")
            elif new_settings == letter_settings:
                temp2 = letter_settings
                letter_settings = input("Введите новый символ: ")
                if (letter_settings == letter_sum_numbers
                        or letter_settings == letter_count_numbers
                        or letter_settings == letter_zero_users
                        or letter_settings == letter_average):
                    letter_settings = temp2
                    temp2 = ""
                    print("Данный символ сейчас недоступен")
            elif new_settings == "Y":
                letter_sum_numbers = "A"
                letter_count_numbers = "B"
                letter_zero_users = "C"
                letter_average = "D"
                letter_settings = "F"
                user_action = ""
                break
            elif new_settings == "S":
                user_action = ""
                break
            else:
                print("Неверный символ, попробуйте еще раз")

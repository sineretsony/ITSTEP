from random import randint

# Задание 1

num1 = 0
num2 = 0

try:
    num1 = int(input("Введите число x: "))
    num2 = int(input("Введите число y: "))

    if num1 == 0 or num2 == 0:
        raise ZeroDivisionError
except ValueError:
    print("Операция производится только с числами!")
except ZeroDivisionError:
    print("С нулями операции не проводятся")
else:
    resul_xy = num1 ** num2
    print(f"Значение {num1} в степени {num2}, равно {resul_xy} ")
finally:
    print("Программа завершена")

# Задание 2

num3 = input("Введите целое число: ")
result = ""

try:
    num3 = int(num3)
    while num3 > 0:
        digit = num3 % 10
        if digit != 3 and digit != 6:
            result = str(digit) + result
        num3 //= 10
    print("Результат:", result)
except ValueError:
    print("Операция производится только с числами!")

# Задание 3

while True:
    try:
        num4 = float(input("Введите первое число: "))
        num5 = float(input("Введите второе число: "))
        operator = input("Введите операцию (+, -, *, /): ")

        if operator in ('+', '-', '*', '/'):
            if operator == '+':
                result = num4 + num5
            elif operator == '-':
                result = num4 - num5
            elif operator == '*':
                result = num4 * num5
            elif operator == '/':
                if num5 != 0:
                    result = num4 / num5
                else:
                    raise ZeroDivisionError("Ошибка: деление на ноль!")
            print(f"Результат: {result}")
        else:
            print("Недопустимая операция. Пожалуйста, введите +, -, *, или /.")

        new_calcul = input(
            "Хотите выполнить еще одну операцию? (да/нет): ")
        if new_calcul != 'да':
            break
    except ValueError:
        print("Ошибка: некорректный ввод числа.")
    except ZeroDivisionError as ex:
        print(ex)

# Задание 4

secret_num = ""
count = 0
picking = 0

while count < 4:
    secret_num += str(randint(1, 6))
    count += 1

# print(secret_num)

print("Секретный код сгенерирован. Попробуйте угадать!")

while True:
    try:
        picking = int(input("Введите 4-значное число от 1 до 6: "))
    except ValueError:
        print("Требуется ввести цифры от 1 до 6")
    except:
        print("Произошла ошибка, попробуйте еще раз")

    if 1111 <= picking <= 6666:
        correct = 0
        misp = 0
        temp_secret = int(secret_num)

        count2 = 0
        while count2 < 4:
            d_picking = picking % 10
            d_secret = temp_secret % 10

            if d_picking == d_secret:
                correct += 1
            elif (d_picking == temp_secret // 1000 or
                  d_picking == (temp_secret // 100) % 10 or
                  d_picking == (temp_secret // 10) % 10 or
                  d_picking == temp_secret % 10):
                misp += 1

            picking //= 10
            temp_secret //= 10
            count2 += 1

        print(f"Верные цифры: {correct}, неправильные цифры: {misp}")

        if correct == 4:
            print("Поздравляем, вы угадали секретный код!")
            break
    else:
        print("Пожалуйста, введите 4-значное число от 1 до 6.")

# Задача 1

num1 = 0
num2 = 0
num3 = 0
info = "число"
operator = ""

while not operator:
    quest = input(f"Введите {info}: ")
    if num1 == 0:
        num1 = int(quest)
    elif num2 == 0:
        num2 = int(quest)
    elif num3 == 0:
        num3 = int(quest)
    if num3 and info == "число":
        info = "действие +\\*"
    elif num3 and info != "число":
        operator = quest
else:
    if operator == "+":
        print(f"Результат: {num1 + num2 + num3}")
    elif operator == "*":
        print(f"Результат: {num1 * num2 * num3}")

# Задача 2

num4 = 0
num5 = 0
num6 = 0
info2 = "число"
operator2 = ""
result2 = ""

while not operator2:
    quest2 = input(f"Введите {info2}: ")

    if num6 and info2 == "действие макс\\мин\\среднее":
        operator2 = quest2

    if num4 == 0:
        num4 = int(quest2)
    elif num5 == 0:
        num5 = int(quest2)
    elif num6 == 0:
        num6 = int(quest2)
        info2 = "действие макс\\мин\\среднее"

if operator2 == "макс":
    print(max(num4, num5, num6))
elif operator2 == "мин":
    print(min(num4, num5, num6))
elif operator2 == "среднее":
    print((num4 + num5 + num6) / 3)

# Задача 3
meters = float(input("Введите количество метров: "))
choice = input("Выберите перевод (мили, дюймы, ярды): ")

if choice == "мили" or choice == "Мили":
    miles = meters * 0.000621371
    print(f"{meters} метров = {miles} миль")
elif choice == "дюймы" or choice == "Дюймы":
    inches = meters * 39.3701
    print(f"{meters} метров = {inches} дюймов")
elif choice == "ярды" or choice == "Ярды":
    yards = meters * 1.09361
    print(f"{meters} метров = {yards} ярдов")
else:
    print("Неверный выбор перевода.")

# Задача 4

day_number = int(input("Введите номер дня недели (1-7): "))

if day_number == 1:
    print("Название дня недели: понедельник")
elif day_number == 2:
    print("Название дня недели: вторник")
elif day_number == 3:
    print("Название дня недели: среда")
elif day_number == 4:
    print("Название дня недели: четверг")
elif day_number == 5:
    print("Название дня недели: пятница")
elif day_number == 6:
    print("Название дня недели: суббота")
elif day_number == 7:
    print("Название дня недели: воскресенье")
else:
    print("Неверный номер дня недели.")


# Задача 5

month_number = int(input("Введите номер месяца (1-12): "))

if month_number == 1:
    print("Название месяца: январь")
elif month_number == 2:
    print("Название месяца: февраль")
elif month_number == 3:
    print("Название месяца: март")
elif month_number == 4:
    print("Название месяца: апрель")
elif month_number == 5:
    print("Название месяца: май")
elif month_number == 6:
    print("Название месяца: июнь")
elif month_number == 7:
    print("Название месяца: июль")
elif month_number == 8:
    print("Название месяца: август")
elif month_number == 9:
    print("Название месяца: сентябрь")
elif month_number == 10:
    print("Название месяца: октябрь")
elif month_number == 11:
    print("Название месяца: ноябрь")
elif month_number == 12:
    print("Название месяца: декабрь")
else:
    print("Неверный номер месяца.")


# Задача 6

number = float(input("Введите число: "))

if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is equal to zero")

# Задача 7

number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))

if number1 == number2:
    print("Числа равны.")
elif number1 < number2:
    print(f"Числа в порядке возрастания: {number1}, {number2}")
else:
    print(f"Числа в порядке возрастания: {number2}, {number1}")

# Задача 8

phone_conv = int(input("Введите длительность разговора мин: "))

phone_op = input("Введите свой оператор 'LIFE (1), "
                 "Vodafone (2), Kyivstar (3)': ")
phone_op2 = input("Введите оператор собеседника 'LIFE (1), "
                  "Vodafone (2), Kyivstar (3)': ")

cost_life = 0.05
cost_vodafone = 0.07
cost_kyivstar = 0.06
cost_minute = 0

if (phone_op == "1" and phone_op2 == "1") or \
   (phone_op == "2" and phone_op2 == "2") or \
   (phone_op == "3" and phone_op2 == "3"):
    cost_minute = min(cost_life, cost_vodafone, cost_kyivstar)
elif (phone_op == "1" and (phone_op2 == "2" or phone_op2 == "3")) or \
     (phone_op == "2" and (phone_op2 == "1" or phone_op2 == "3")) or \
     (phone_op == "3" and (phone_op2 == "1" or phone_op2 == "2")):
    cost_minute = cost_life
elif (phone_op == "2" and phone_op2 == "1") or \
     (phone_op == "3" and phone_op2 == "1"):
    cost_minute = cost_vodafone
elif (phone_op == "1" and phone_op2 == "3") or \
     (phone_op == "2" and phone_op2 == "3"):
    cost_minute = cost_kyivstar
else:
    print("Неверный выбор оператора.")

total_cost = phone_conv * cost_minute
print(f"Стоимость разговора: {total_cost} грн")

# Задача 9

salary = 200
manager1 = 0
manager2 = 0
manager3 = 0
count = 1

'''С функциями пайтон я немного сталкивался (плюс мы на js с ними работали), 
поэтому решил добавить чтобы не плодить много условий. 
Я бы всё равно их копировал, а не писал с нуля 😁
---------------------------------------------------------------------
Передаём (m)--> доход и (s)--> ставка --- > возвращает ставка + % '''


def salary_manager(m, s):
    if m < 500:
        temp = m * 0.03
    elif 500 <= m < 1000:
        temp = m * 0.05
    else:
        temp = m * 0.08
    temp += s
    return temp


while not manager3:
    income = int(input(f"Введите доход менеджера {count}: "))
    if manager1 == 0:
        manager1 = income
    elif manager2 == 0:
        manager2 = income
    elif manager3 == 0:
        manager3 = income
    count += 1

manager1 = salary_manager(manager1, salary)
manager2 = salary_manager(manager2, salary)
manager3 = salary_manager(manager3, salary)


print(f"Зарплаты менеджеров\n"
      f"Менеджер 1 зарплата {manager1}\n"
      f"Менеджер 2 зарплата {manager2}\n"
      f"Менеджер 3 зарплата {manager3}")

if manager2 < manager1 > manager3:
    manager1 += salary
    print(f"Премию получает Менеджер 1 в размере {salary} зарплата {manager1}")
elif manager1 < manager2 > manager3:
    manager2 += salary
    print(f"Премию получает Менеджер 2 в размере {salary} зарплата {manager2}")
elif manager1 < manager3 > manager2:
    manager3 += salary
    print(f"Премию получает Менеджер 3 в размере {salary} зарплата {manager3}")


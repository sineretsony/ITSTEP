# Задание 1
num = 2.99
print(int(num))

# Задание 2
# kol = int(input("Введите целое число: "))
kol = int(5)
print(kol)

# Задание 3
# radius = float(input("Введите число: "))
radius = float(1.1)
print(radius)

# Задание 4
radius2 = 1.1
print(f"r = {radius2} Area = {3.14159265359 * radius2 ** 2}")
print(f"r = {radius2} Area = {int(3.14159265359 * radius2 ** 2)}")

# Задание 5
# x_sleep = int(input("Вася обычно спит ночью X часов: "))
x_sleep = 1
# y_sleep = int(input("Устраивает себе днем тихий час на Y минут: "))
y_sleep = 60

results = int((x_sleep * 60) + y_sleep)
print(f"Вася спит: {results} минут")

# Задание 6
# times = int(input("Введите кол-во сек: "))
times = 3601
hour = times // 3600
hour_x = times % 3600
minutes = hour_x // 60
sec = hour_x % 60
print(f"Время: {hour} часов, {minutes} минут, {sec} секунд")



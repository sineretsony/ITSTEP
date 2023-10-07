print("test")

name = "McGregor"
number = 10
number1 = 10.2
print(type(number))
print(type(number1))

print(4 / 2.0)

number3 = input("Enter num: ")
print("number", int(number3)*2)

num = 3
print(f"num {num}")

a = 10
b = 2

sum_result = a + b
difference_result = a - b
product_result = a * b
quotient_result = a / b

print("Сумма:", sum_result)
print("Разность:", difference_result)
print("Произведение:", product_result)
print("Частное:", quotient_result)

c = 15
d = 2

result = c + d
print(f"Результат: {result}")


distance = float(input("Введите расстояние до аэропорта (в км): "))
time = float(input("Введите время в пути (в часах): "))

speed = distance / time
print(f"Ехать нужно со скоростью: {speed} км/ч.")

start_h = int(input("Введите час начала: "))
start_min = int(input("Введите минуту начала: "))
start_sec = int(input("Введите секунду начала: "))

end_h = int(input("Введите час завершения: "))
end_min = int(input("Введите минуту завершения разговора: "))
end_sec = int(input("Введите секунду завершения разговора: "))

start_seconds = start_h * 3600 + start_min * 60 + start_sec
endSeconds = end_h * 3600 + end_min * 60 + end_sec
seconds = endSeconds - start_seconds
cos = 0.30
cop = (seconds / 60) * cos

print("Стоимость разговора:", cop, "грн.")


dist = float(input("Расстояние поездки км: "))
fuel = float(input("Расход топлива на 100 км в литрах: "))
pr_1 = float(input("Введите стоимость первого вида: "))
pr_2 = float(input("Введите стоимость второго вида: "))
pr_3 = float(input("Введите стоимость третьего вида: "))

sht = (fuel / 100) * dist

cost_1 = sht * pr_1
cost_2 = sht * pr_2
cost_3 = sht * pr_3

print(f"1-й вид бензина: {cost_1:.2f} грн.")
print(f"2-й вид бензина: {cost_2:.2f} грн.")
print(f"3-й вид бензина: {cost_3:.2f} грн.")



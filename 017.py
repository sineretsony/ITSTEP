# numbers = [1, 2, 3, 4, 5]
# students = list(("styd1", "styd2", "styd3"))
#
# print(numbers, students)
#
# array = [1, 2, 3, 4, "5", "6"]
# print(array)
#

# months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль",
#           "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
# sums = [12345, 14532, 17523, 23421, 21345, 32124, 36214, 34214,
#         31245, 30123, 29313, 20235]
#
# total_income = 0
# average = 0
#
# min_i = 0
# max_i = 0
# min_month = ""
# max_month = ""
#
#
# for i in range(len(sums)):
#     total_income += sums[i]
#     if sums[i] > max_i:
#         max_i = sums[i]
#         max_month = months[i]
#     if sums[i] < min_i:
#         min_i = sums[i]
#         min_month = months[i]
#
# if len(sums) > 0:
#     average = total_income / len(sums)
#
# print("Общий доход за год:", total_income)
# print("Средний доход:", average)
# print("Наибольший доход", max_month, "с суммой", max_i)
# print("Наименьший доход", min_month, "с суммой", min_i)

# list1 = [i*i for i in range(0, 6)]
# print(list1)
#
# list2 = [i + "." for i in "python"]
# print(list2)
#
# list3 = [i*i for i in range(1, 11) if i % 2 == 0]
# print(list3)

# category = ["Drama", "Comedy"]
# print("---------------------")
# category.append("Fantasy")
# print(category)
# print("---------------------")
# category.extend(["Mystery", "Triller"])
# print(category)
# print("---------------------")
# category.insert(0, "Action")
# print(category)
# print("---------------------")
# category.remove("Action")
# print(category)
# print("---------------------")
# category.pop(0)
# print(category)
# print("---------------------")
# # category.clear()
# # print(category)
#
# print(category.index("Mystery"))
# print(category.count("Mystery"))
#
# category.sort()
# category.reverse()
# print(category)

# Задание 1
arr = [2, -3, 5, 7, -1, 8, 4, -6]
negative_sum = 0
for num in arr:
    if num < 0:
        negative_sum += num
print("Сумма отрицательных элементов:", negative_sum)

min_value = 0
max_value = 0
min_index = 0
max_index = 0
for i in range(len(arr)):
    num = arr[i]
    if num < min_value:
        min_value = num
        min_index = i
    if num > max_value:
        max_value = num
        max_index = i
product_min_max = 1
start_index = min(min_index, max_index)
end_index = max(min_index, max_index)
for i in range(start_index + 1, end_index):
    product_min_max *= arr[i]
print("Произведение элементов между min и max элементами:", product_min_max)

prod = 1
for i in range(0, len(arr), 2):
    prod *= arr[i]
print("Произведение элементов с четными номерами:", prod)

first_n_in = -1
last_n_in = -1
for i in range(len(arr)):
    num = arr[i]
    if num < 0:
        if first_n_in == -1:
            first_n_in = i
        last_n_in = i
if first_n_in != -1 and last_n_in != -1:
    sum_first_last_ns = 0
    for i in range(first_n_in + 1, last_n_in):
        sum_first_last_ns += arr[i]
    print("Сумма между первым и последним отрицательными:", sum_first_last_ns)
else:
    print("В массиве нет отрицательных элементов.")

# Задание 2

arr2 = [i for i in range(0, 10)]
arr3 = []
arr4 = []

for i in arr2:
    if len(arr3) != len(arr2) // 2:
        arr3.append(i)
    else:
        arr4.append(i)

print(arr2)
print(arr3)
print(arr4)

# Задание 3

arr5 = []

for i in range(5):
    arr5.append(arr3[i] * arr4[i])

print(arr5)
 











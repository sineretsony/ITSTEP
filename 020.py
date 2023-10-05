# stud = [2000, 1999, 2005]
# studAge = list(map(lambda x: 2023-x, stud))
#
# print(studAge)
#

# adminPassw = "111"
# studPassw = "222"
#
#
# def userLogIn(userLog, userPass):
#     if (userLog.lower() == "admin") and (userPass == adminPassw):
#         print("Welcome Admin")
#     elif (userLog.lower() == "student") and (userPass == adminPassw):
#         print("stud")
#     else:
#         print("Ошибка")
#
#
# def changePass(userLog, userPass):
#     global adminPassw, studPassw
#     if (userLog.lower() == "admin") and (userPass == adminPassw):
#         adminPassw = input("Введите новый пароль ")
#     elif (userLog.lower() == "student") and (userPass == adminPassw):
#         studPassw = input("Введите новый пароль ")
#     else:
#         print("Ошибка")
#
#
# def userAction(login, passw, action):
#     return action(login, passw)
#
#
# # userAction("admin", "111", userLogIn)
#
# def nameUpper(name):
#     return "user" + name.upper()
#
#
# def nameLower(name):
#     return "user" + name.lower()
#
#
# def makeLog(userName, maker):
#     return maker(userName)
#
#
# print(makeLog("bob", nameLower))

# userLogs = ["Admin", "STUDENT", "TeacheR"]
# userLogsLow = []
# # for i in userLogs:
# #     userLogsLow.append(i.lower())
#
#
# userLogsLow2 = list(map(str.lower, userLogs))
# print(userLogsLow2)
#
# myValues = ["2", "3", "5", "123"]
# myNums = list(map(int, myValues))
# print(myNums)
#
# myDigits = list(map(lambda x: int(x), myNums))
# print(myDigits)
#
# pizzaTypes = ["Gava", "Marga", "Pip"]
#
#
# def modyfyizza(type):
#     return type + " Pizza"
#
#
# pizzaNames = list(map(modyfyizza, pizzaTypes))
# print(pizzaNames)
#
# mums = [10, 20, 30]
# mums2 = [1, 2, 3]
#
# result = map(lambda a, b: a ** b, mums, mums2)
# print(list(result))

# prices = [100, 8, 45, 60, 34]
# expensiv = list(filter(lambda x: x > 50, prices))
# print(expensiv)
#
# userLogs = ["123user1", "userSt", "123sdsd", "admin"]
#
#
# def checkLog(user):
#     if user.lower().find("user") != -1:
#         return True
#     else:
#         return False
#
#
# trueUser = list(filter(checkLog, userLogs))
# print(trueUser)

userLogs2 = ["123user1", "userSt", "123sdsd", "admin"]
userPassw = ["123", "2332", "3434", "7765"]

# for log, passw in zip(userLogs2, userPassw):
#     print(f"log: {log}, passw: {passw}")
#
# from functools import reduce
#
# prices2 = [100, 8, 45, 60, 34]
#
#
# def mySum(x, y):
#     return x + y
#
#
# result2 = reduce(mySum, prices2,
#                  0)  # 0 если колекция пустая вернёт 0 без нуля бедет ексепшен
# print(result2)
#
# result3 = reduce(lambda a, b: a + b, prices2, 0)
# print(result3)
#
# words = ['phyton', "is", "cool"]
#
# result4 = reduce(lambda a, b: a + b if a == "" else a + " " + b, words, "")
# print(result4)

# Задание 1
num = [1, 2, 3, 4, 5]

print(list(map(lambda n: n * n, num)))

# Задание 2
fruit = ["apple", "banana", "cherry"]
print(list(map(lambda f: len(f), fruit)))

# Задание 3
num2 = [1, 2, 3, 4, 5]
print(list(filter(lambda a: a % 2 == 0, num2)))

# Задание 4
fruit2 = ["apple", "banana", "cherry"]
print(list(filter(lambda l: l[0].lower() == "a", fruit2)))

# Задание 5
num3 = [1, 2, 3, 4, 5, 6, "5", "2", "66", "e"]

conv = list(map(lambda x: int(x) if str(x).isdigit() else x, num3))
filtered_numbers = list(
    filter(lambda x: str(x).isdigit() and int(x) % 3 == 0, conv))

print(filtered_numbers)

# Задание 6
num4 = [1, 2, 3]
num5 = [4, 5, 6]

for a, b in zip(num4, num5):
    print(f"list1 = {a} list2 {b}")

# Задание 7
print(list(map(lambda a, b: a * b, num4, num5)))

# Задание 8
num6 = [(1, 2), (3, 1), (4, 4), (5, 3)]
print(list(filter(lambda a: a[0] > a[1], num6)))

# Задание 9
from functools import reduce

num7 = [1, 2, 3, 4, 5]


def multiply(x, y):
    return x * y


print(reduce(multiply, num7))

# Задание 10
num8 = [1, 2, 3, 4, 5]


def maxN(x, y):
    return max(x, y)


print(reduce(maxN, num8))

# Задание 11
num9 = [1, 2, 3, 4, 5, 4, 4]

from functools import reduce


def count_occurrences(ac, count, element):
    if element == count:
        return ac + 1
    else:
        return ac


print(reduce(lambda ac, element: count_occurrences(ac, 4, element), num9, 0))

# Задание 12
num10 = [1, 2, 3, 4, 5]
status = [True, False, True, False, True]


def filter_zip(a, s):
    return [x for x, y in zip(a, s) if y]


result = filter_zip(num10, status)
print(result)

# Задание 13
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

print(list(filter(lambda lst: 5 in lst, lists)))

# Задание 14
words = ["apple", "banana", "cherry", "date", "elderberry"]

print(list(filter(lambda word: len(word) > 6, words)))

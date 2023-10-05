# def rFactorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * rFactorial(n - 1)
#
#
# print(rFactorial(5))
#
#
# def isStrPalindrom(myStr):
#     if len(myStr) == 0:
#         return True
#     else:
#         if myStr[0] == myStr[-1]:
#             return isStrPalindrom(myStr[1:-1])
#         else:
#             return False
#
#
# print(isStrPalindrom("madam"))
#
#
# def findMin(numlist):
#     if len(numlist) > 1:
#         return min(findMin(numlist[:-1]), numlist[-1])
#     else:
#         return numlist[0]
#
#
# lst = [2, 4, 1, 8, 3]
#
# print(findMin(lst))

# def sumNum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sumNum(n - 1)
#
#
# n = int(input("Введите число n: "))
# result = sumNum(n)
# print(f"Сумма чисел от 1 до {n} равна {result}")
#
#
# def sumNumNum(n):
#     if n < 10:
#         return n
#     else:
#         l_di = n % 10
#         r_di = n // 10
#         return l_di + sumNumNum(r_di)
#
#
# n2 = int(input("Введите целое число: "))
# result = sumNumNum(n2)
# print(f"Сумма цифр числа {n2} равна {result}")


# def add(x):
#     return x + 10
#
#
# nums = [1, 2, 3]
# for i in nums:
#     print(add(i))
#
# newNum = lambda x: x + 10
#
# for i in nums:
#     print(newNum(i))
#
# for i in nums:
#     print((lambda x: x + 10)(i))

# students = [
#     ["Bob", 10],
#     ["Kate", 9],
#     ["Andry", 6],
# ]
#
# print(students)
# sortedStudents = sorted(students, key=lambda x: x[1])
# print(sortedStudents)
#
# grnToDollar = 38
# discount = 0.15
#
# priceDol = lambda x: x / grnToDollar * (1 - discount)
# priceGrn1 = float(input("price in grn: "))
# print("price $ = ", priceDol(priceGrn1))

# userName = lambda firstName, lastName: f"Full name is: {firstName.title()} {lastName.title()}"
#
# print(userName("ilon", "mask"))
#
#
# add = lambda a, b = 1: a + b
# print(add(2, 2))

# Задание 1
lst = [(lambda i: i * 2)(i) for i in range(1, 5)]
print(lst)

# Задание 2
input_str = input("Введите список чисел, через пробел: ")


# Задание 3


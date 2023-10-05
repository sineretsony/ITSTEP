# def test():
#     a = 9
#     b = 0
#     return a, b
#
#
# print(list(test()))
#
#
# def calcSum(*args):
#     sum = 0
#     count = 0
#     for i in args:
#         sum += i
#         count += 1
#     return sum / count
#
#
# print("avg = ", calcSum(2, 2, 2))
#
#
# def sumNums(**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(key, value)
#
#
# sumNums(num=1, num2=2)
#
#
# def userGr(login, passw="111"):
#     if login == "admin":
#         print("Wa")
#     elif login == "stud":
#         print("St")
#     else:
#         print("Walkome")
#
#
# userGr("admin", passw="123")
#
#
# def calcExample():
#     localVar = int(input("Введите число: "))
#     resultVar = localVar ** 2
#     print(resultVar)
#
#
# calcExample()


# userNAME = "admin"
# def chackLogin():
#     userNAME = 0

# def outerFunc():
#     localVar = 2
#
#     def innerFunc():
#         nonlocal localVar
#         localVar = 3
#         print(localVar)
#
#     innerFunc()
#
#
# outerFunc()
#
# customers = ["UserJane", "Bob", "admiNBill"]
#
#
# def sayHello(customer):
#     if customer.find("admin") != -1:
#         print("hello admin", customer)
#     elif customer.find("user") != -1:
#         print("hello user", customer)
#     else:
#         print("Hello", customer)
#
#
# def greetings(customList, greetFunc):
#     for c in customList:
#         greetFunc(c.lower())
#
#
# greetings(customers, sayHello)

# # Задание 1
# text1 = ("Don't compare yourself with anyone in this world… "
#          "if you do so, you are insulting yourself.")
# author = "Bill Gates"
#
#
# def formatted_quote(t, a):
#     form_text = f'“{t}” {a}'
#     print(form_text)
#
#
# formatted_quote(text1, author)
#
# # Задание 2
# num1 = 5
# num2 = 50
#
#
# def pairedNum(o, t):
#     for i in range(o, t):
#         if i % 2 == 0:
#             print(i)
#
#
# pairedNum(num1, num2)
#
#
# # Задание 3
# def draw_square(side_l, s, sf):
#     if sf:
#         for _ in range(side_l):
#             print(s * side_l)
#     else:
#         for i in range(side_l):
#             if i == 0 or i == side_l - 1:
#                 print(s * side_l)
#             else:
#                 print(s + " " * (side_l - 2) + s)
#
#
# draw_square(5, "■", True)
#
#
# # Задание 4
# def find_minimum(*args):
#     if not args:
#         return None
#     return min(args)
#
#
# result = find_minimum(5, 3, 9, 2, 7)
# print("Минимальное значение:", result)

# Задание 5

def palindrome(p):
    p_str = str(p)
    pal = p_str[::-1]
    return p_str == pal


print(palindrome(1234))
print(palindrome(1221))


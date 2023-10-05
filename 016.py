# myStr = "python was created in the late 1980's by Guido van Rossum."
# print(myStr)
# print(myStr.swapcase())
# print(myStr.capitalize())
# print(myStr.title())
# print(myStr.lower())
# print(myStr.upper())
#
# myStr = ("Python was created in the late 1980's  by Guido van Rossum. Python- "
#          "cool!")
#
# str1 = "hello python"
#
# print(type(str1))
# print("str1 = ", str1)
# print(id(str1))
#
# str1 = "hello js "
# print("str1 = ", str1)
# print(id(str1))
#
# str2 = '''Python was created in the late 1980's
#  by Guido van Rossum. Python- cool!
# '''
#
# str3 = 'Python was\n created in the \tlate 1980\
#  by Guido van Rossum. Python- cool!\
# '
#
# print(str3)
#
# print("one" + "two")
# print("1" * 3)
#
# str4 = "foobar"
# print(str4[0])
# print(str4[1])
#
# print(len(str4))
#
# print(str4[len(str4) - 1])
#
# print(str4[-1])
#
# print(str1[:-1:1])
#
# print(myStr)
# print(myStr.capitalize())
# print(myStr.lower())
# print(myStr.upper())
# print(myStr.title())
# print(myStr)
#
# print("find python", myStr.find('Python', 20, 50))
# print("find python", myStr.rfind('Python'))
# # print("find python", myStr.index('P1ython')) # valueerror
# print(len(myStr))
#
# print(myStr.startswith('Python2'))
#
# strNum = "\n\n\t"
# print(strNum.isnumeric())
# print(strNum.islower())
# print(strNum.isspace())
#
# testStr = "  python \t\tjs  "
# print(testStr)
# print(testStr.strip())
# print(testStr.lstrip())
# print(testStr.expandtabs(tabsize=1))
#
# print(testStr.ljust(20, "-"))
# print(testStr.center(50, '*'))
#
# print(myStr.count("Python"))
# print(myStr.replace("Python", "Js", 1))
#
# print(myStr.split('.'))
#
# print("".join(("one", "two")))

# user_str = input("Введите строку: ")
# print(user_str[::-1])
#
# user_str2 = input("Введите строку: ")
# results = ""
#
# for i in user_str2[::-1]:
#     results += i
# print(results)

# # Задание 2
# user_str = input("Введите строку: ")
# num = 0
# let = 0
# other = 0
#
# for i in user_str:
#     if i.isdigit():
#         num += 1
#     elif i.isalpha():
#         let += 1
#     else:
#         other += 1
#
# print(f"Букв в строке {let}\n Цифр в строке {num}\nДругие символов {other}")

# # Задание 3/4
#
# user_str = input("Введите строку: ")
# user_search = input("Введите символ/слово для поиска: ")
#
# print("Символ встречается ", user_str.lower().count(user_search.lower()))
#
# # Задание 5
#
# user_str2 = input("Введите строку: ")
# user_search2 = input("Введите символ/слово для поиска: ")
# user_replace = input("Введите символ/слово для замены: ")
#
# print(user_str2.replace(user_search2, user_replace))

# Задание 6

text = ('на улице начался дождь! 5 кошек бежали к дому.\nсобака стояла под '
        "деревом, смотря на небо.\nветер свистел в ветвях, а капли дождя "
        "барабанили по крыше.\nна полке в доме стояла кружка с горячим "
        "шоколадом.\nчудесно, - подумал я, сидя у окна и наблюдая "
        'за этой картиной.')

num2 = 0
num_p = 0
num_ex = 0

for i in text:
    if i.isdigit():
        num2 += 1
    elif i in '.,?:;':
        num_p += 1
    elif i == '!':
        num_ex += 1

print("Измененный текст:")
print(text.title())

print(f"Количество цифр в тексте: {num2}")
print(f"Количество знаков препинания в тексте: {num_p}")
print(f"Количество восклицательных знаков в тексте: {num_ex}")

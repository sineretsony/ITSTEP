# try:
#     data_file = open('data.txt')
#     if data_file:
#         print("File is open")
#         # print(data_file.read(10))
#         # print(data_file.read(10))
#         # rowStr = repr(data_file.read())
#         # print(rowStr)
#         # print(data_file.readline())
#         # print(data_file.readlines())
#         # for line in data_file:
#         #     print(line)
# except:
#     print("We can't open file")


# file = open('data.txt', 'w+')
# count = file.write('Process finished with exit code 0')
# print(f'we wrote {count}, symbols')
#
# file.close()
#
# file = open('data.txt', 'w')
# for i in range(5):
#     file.write(f"Line {i + 1} \n")
#
# file.close()
# file = open('data.txt', 'w')
# mysters = ['first', 'second']
# file.writelines(mysters)
# file.close()
#
#
# with open('data.txt', 'r') as file:
#     print(file.read())
#
# with open('data.txt', 'r') as fil1, open('data2.txt', 'w') as file2:
#     data = fil1.read()
#     file2.write(data)


# def replaceTextInFile(fileName, originalTxt, newTxt):
#     with open(fileName) as file:
#         data = file.read()
#         data = data.replace(originalTxt, newTxt)
#
#     with open(fileName, 'w') as file:
#         file.write(data)
#
#
# def readFile(fileName):
#     with open(fileName) as file:
#         data = file.read()
#         print(data)
#
#
# readFile('data.txt')
# replaceTextInFile('data.txt', 'first', 'fdfdsfsdf')
# readFile('data.txt')
#

# def wordCounter(fileName):
#     nWords = 0
#     with open('data.txt') as fila:
#         data = fila.read()
#         lines = data.split()
#         for i in lines:
#             if not i.isnumeric():
#                 nWords += 1
#     return nWords
#
#
# print(wordCounter('data.txt'))
#
#
# def removeLine(fileIn, fileOut, lineNum):
#     with open(fileIn) as file:
#         lines = file.readlines()
#         counter = 1
#         with open(fileOut, 'w') as fileO:
#             for line in lines:
#                 if counter != lineNum:
#                     fileO.write(line)
#                     counter += 1
#
#
# removeLine('data.txt', 'data2.txt', 5)


# # Задание 1
# temp_list = []
#
# with open('data.txt', 'r', encoding='utf-8') as file:
#     data = file.readlines()
#     avr = 0
#     summ = 0
#     for d in data:
#         words = d.strip().split(' ')
#         last_word = words[-1]
#         avr += 1
#         summ += int(last_word)
#         if last_word.isdigit():
#             if int(last_word) < 3:
#                 temp_list.append(d)
#
# print("Ученики с оценкой меньше 3:")
# for item in temp_list:
#     print(item.strip())
#
# print("Средняя оценка ", summ / avr)

# # Задание 2
# file = open('data.txt', 'a', encoding='utf-8')
#
# while True:
#     lines = input("Введите строку для записи: ")
#     if lines == '':
#         print("Файл закрыт")
#         file.close()
#         break
#     file.write(lines + '\n')

# # Задание 3
# with open('data.txt', 'r', encoding='utf-8') as file:
#     data = file.readlines()
#     print('Строк в файле: ', len(data))
#     count = 0
#     for l in data:
#         count += 1
#         print(f'В строке {count}, символов {len(l)}')



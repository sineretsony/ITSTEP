# Задание 1
pal_input = input("Введите слово на проверку палиндрома: ")

pal_lower = pal_input
other_char = " ,."

for i in other_char:
    pal_lower = pal_lower.lower().replace(i, "")

pal_mirror = pal_lower[::-1]

if pal_mirror == pal_lower:
    print(f"Ваше слово: '{pal_input}' — палиндром!")
else:
    print(f"Слово: '{pal_input}' не является палиндромом, попробуйте еще")


# Задание 2
input_text = input("Введите текст: ")
input_list = input("Введите список слов через пробел: ")

text_split = input_text.split()
text_list = input_list.split()

new_text = ""
for w in text_split:
    if w in text_list:
        new_text += w.upper() + " "
    else:
        new_text += w + " "

new_text = new_text.strip()

print(new_text)

# Задание 3
input_text2 = '''Сегодняшний день принес с собой свежий ветер перемен,
который напомнил нам о быстротечности времени! Под лучами утреннего солнца
природа оживала, расцветая во всей своей красе. В такие моменты становится
понятно, как важно находить радость в мелочах и ценить каждый момент жизни.'''

count_sent = 0
current = ""
for c in input_text2:
    if c in ['.', '!', '\t']:
        if current:
            count_sent += 1
        current = ""
    else:
        current += c

print(f"В вашем тексте: {count_sent} предложений")

# Задание 4
result = 0
while True:
    try:
        num4 = input("Введите выражение для решения: ")
        num5 = ""
        num6 = ""
        operator = ""

        for i in num4:
            if i.isdigit() and len(operator) == 0:
                num5 += i
            elif i.isdigit() and len(num5) > 0:
                num6 += i
            elif i in ('+', '-', '*', '/'):
                operator += i

        if operator in ('+', '-', '*', '/'):
            num5 = float(num5)
            num6 = float(num6)

            if operator == '+':
                result = num5 + num6
            elif operator == '-':
                result = num5 - num6
            elif operator == '*':
                result = num5 * num6
            elif operator == '/':
                if num6 != 0:
                    result = num5 / num6
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


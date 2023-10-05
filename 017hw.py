# Задание 1
def up_letter_sentence(txt):
    result = ""
    temp = ""
    for i in txt:
        temp += i
        if i in [".", "!"]:
            result += temp.title()
            temp = ""
    if len(temp) > 0:
        result += temp.title()
    return result


def char_counting(txt):
    count_s = txt.count(".") + txt.count(",")
    count_n = sum(1 for c in txt if c.isdigit())
    count_e = txt.count("!")
    return count_s, count_n, count_e


def info_text(txt):
    print(up_letter_sentence(txt))
    info = char_counting(txt)
    s, n, e = info
    print(f"В тексте знаков препинания {s},\n"
          f"Чисел {n},\n"
          f"Восклицательных знаков {e}")


info_text("Текст1. текст2! текст. текст")


# Задание 2 и 3
def search_value(lst, search):
    result = lst.count(search)
    return result


def calculate_sum(lst):
    return sum(lst)


def calculate_average(lst):
    if len(lst) == 0:
        return 0
    return sum(lst) / len(lst)


def start_search():
    try:
        input_str = input("Введите элементы списка через запятую: ")
        lst_numbers = [int(x) for x in input_str.split(",")]

        search_num = int(input("Введите число для поиска: "))
        count = search_value(lst_numbers, search_num)

        print(f"Число {search_num} встречается в списке {count} раз.")

        total_sum = calculate_sum(lst_numbers)
        print(f"Сумма всех чисел в списке: {total_sum}")

        average = calculate_average(lst_numbers)
        print(f"Среднее арифметическое всех чисел в списке: {average}")
    except ValueError:
        print("Ошибка: Введены некорректные данные. "
              "Пожалуйста, введите целые числа, разделенные запятой.")


start_search()

# Задание 4
warehouse = ["игрушка 1", "игрушка 2", "гирлянда 1", "гирлянда 2", "хлопушка"]
price = [56, 62, 430, 370, 4]
quantity = [20, 10, 4, 5, 2]
total_revenue = 0

while True:
    print("Список товаров в магазине:")
    i = 0
    for item in warehouse:
        i += 1
        print(f"{i}. {item} - {price[i - 1]} грн. (осталось {quantity[i - 1]})")

    cart = []
    cart_total = 0

    while True:
        try:
            choice = int(
                input("Выберите товар (номер) или 0 для завершения покупок: "))
            if choice == 0:
                break
            elif choice < 1 or choice > len(warehouse):
                print("Пожалуйста, выберите правильный номер товара.")
            else:
                quantity_to_buy = int(input(
                    f"Введите количество товара '{warehouse[choice - 1]}': "))
                if quantity_to_buy <= 0:
                    print("Пожалуйста, введите корректное количество.")
                elif quantity_to_buy > quantity[choice - 1]:
                    print("Извините, недостаточно товара на складе.")
                else:
                    cart.append((choice - 1, quantity_to_buy))
                    cart_total += price[choice - 1] * quantity_to_buy
                    quantity[choice - 1] -= quantity_to_buy
        except ValueError:
            print("Пожалуйста, введите корректное число.")

    if len(cart) > 0:
        print(f"Сумма вашей покупки: {cart_total} грн.")
        discount = 0.1 if cart_total >= 1000 else 0
        cart_total *= (1 - discount)
        total_revenue += cart_total
        print(f"С учетом скидки: {cart_total} грн.")

    print(f"Общая выручка магазина: {total_revenue} грн.")

    another_customer = input("Обслужить следующего клиента? (да/нет): ")
    if another_customer.lower() != 'да':
        break




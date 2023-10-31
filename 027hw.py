# Задание 1

class Book:
    def __init__(self, name_book, year, book_publisher, genre, author, cost):
        self._name_book = name_book
        self._year = year
        self._book_publisher = book_publisher
        self._genre = genre
        self._author = author
        self._cost = cost

    def set_name_book(self, new_name_book):
        self._name_book = new_name_book

    def set_year(self, new_year):
        self._year = new_year

    def set_book_publisher(self, new_book_publisher):
        self._book_publisher = new_book_publisher

    def set_genre(self, new_genre):
        self._genre = new_genre

    def set_author(self, new_author):
        self._author = new_author

    def set_cost(self, new_cost):
        self._cost = new_cost

    def get_name_book(self):
        return self._name_book

    def get_year(self):
        return self._year

    def get_book_publisher(self):
        return self._book_publisher

    def get_genre(self):
        return self._genre

    def get_author(self):
        return self._author

    def get_cost(self):
        return self._cost


book1 = Book("Название книги 1", 2000, "Издательство 1",
             "Художественная литература", "Автор 1", 20.99)
book2 = Book("Название книги 2", 2010, "Издательство 2",
             "Документальная литература", "Автор 2", 15.50)
book3 = Book("Название книги 3", 1995, "Издательство 3", "Детектив", "Автор 3",
             18.75)

print("Книга 1:")
print("Название:", book1.get_name_book())
print("Год:", book1.get_year())
print("Издательство:", book1.get_book_publisher())
print("Жанр:", book1.get_genre())
print("Автор:", book1.get_author())
print("Цена:", book1.get_cost())
print()

print("Книга 2:")
print("Название:", book2.get_name_book())
print("Год:", book2.get_year())
print("Издательство:", book2.get_book_publisher())
print("Жанр:", book2.get_genre())
print("Автор:", book2.get_author())
print("Цена:", book2.get_cost())
print()

print("Книга 3:")
print("Название:", book3.get_name_book())
print("Год:", book3.get_year())
print("Издательство:", book3.get_book_publisher())
print("Жанр:", book3.get_genre())
print("Автор:", book3.get_author())
print("Цена:", book3.get_cost())


# Задание 2
class Fraction:
    def __init__(self, numer, denom):
        self.__numer = numer
        self.__denom = denom

    @property
    def numer(self):
        return self.__numer

    @property
    def denom(self):
        return self.__denom

    def set_numerator(self, numer):
        self.__numer = numer

    def set_denominator(self, denominator):
        if denominator != 0:
            self.__denom = denominator
        else:
            print("Знаменатель не может быть нулем.")

    def add(self, ot_fract):
        result_num = self.__numer * ot_fract.denom + ot_fract.numer * self.__denom
        result_denom = self.__denom * ot_fract.denom
        return Fraction(result_num, result_denom)

    def subtract(self, ot_fract):
        result_num = self.__numer * ot_fract.denom - ot_fract.numer * self.__denom
        result_denom = self.__denom * ot_fract.denom
        return Fraction(result_num, result_denom)

    def multiply(self, ot_fract):
        result_num = self.__numer * ot_fract.numer
        result_denom = self.__denom * ot_fract.denom
        return Fraction(result_num, result_denom)

    def divide(self, ot_fract):
        if ot_fract.numer != 0:
            result_num = self.__numer * ot_fract.denom
            result_denom = self.__denom * ot_fract.numer
            return Fraction(result_num, result_denom)
        else:
            print("Деление на нуль")

    def to_string(self):
        return f"{self.__numer}/{self.__denom}"


fract1 = Fraction(1, 2)
fract2 = Fraction(3, 4)

print("Дробь 1:", fract1.to_string())
print("Дробь 2:", fract2.to_string())

result_add = fract1.add(fract2)
print("Результат сложения:", result_add.to_string())

result_sub = fract1.subtract(fract2)
print("Результат вычитания:", result_sub.to_string())

result_multip = fract1.multiply(fract2)
print("Результат умножения:", result_multip.to_string())

result_div = fract1.divide(fract2)
print("Результат деления:", result_div.to_string())


# Задание 3

class Address:
    def __init__(self, street, state, country, zipcode):
        self.__street = street
        self.__state = state
        self.__country = country
        self.__zipcode = zipcode

    @property
    def street(self):
        return self.__street

    @property
    def state(self):
        return self.__state

    @property
    def country(self):
        return self.__country

    @property
    def zipcode(self):
        return self.__zipcode

    def is_valid_zipcode(self):
        return len(str(self.__zipcode)) == 5 and str(self.__zipcode).isdigit()

    def get_full_address(self):
        return (f'Улица: {self.__street}\n'
                f'Штат: {self.__state}\n'
                f'Страна: {self.__country}\n'
                f'Почтовый индекс: {self.__zipcode}\n')


address = Address("1234 Elm St", "California", "USA", 12345)

print("Улица:", address.street)
print("Штат:", address.state)
print("Страна:", address.country)
print("Почтовый индекс:", address.zipcode)
print("Является ли почтовый индекс верным:", address.is_valid_zipcode())
print("Полный адрес:", address.get_full_address())

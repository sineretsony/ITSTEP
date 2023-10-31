# Задание 1
class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError('Знаменатель не может быть равен нулю.')
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        gcd = self.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def __add__(self, other):
        result_numerator = (self.numerator * other.denominator) + (
                other.numerator * self.denominator)
        result_denominator = self.denominator * other.denominator
        result = Fraction(result_numerator, result_denominator)
        result.simplify()
        return result

    def __sub__(self, other):
        result_numerator = (self.numerator * other.denominator) - (
                other.numerator * self.denominator)
        result_denominator = self.denominator * other.denominator
        result = Fraction(result_numerator, result_denominator)
        result.simplify()
        return result

    def __mul__(self, other):
        result_numerator = self.numerator * other.numerator
        result_denominator = self.denominator * other.denominator
        result = Fraction(result_numerator, result_denominator)
        result.simplify()
        return result

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError('Деление на ноль!')
        result_numerator = self.numerator * other.denominator
        result_denominator = self.denominator * other.numerator
        result = Fraction(result_numerator, result_denominator)
        result.simplify()
        return result

    def __iadd__(self, other):
        result = self + other
        self.numerator = result.numerator
        self.denominator = result.denominator
        return self

    def __isub__(self, other):
        result = self - other
        self.numerator = result.numerator
        self.denominator = result.denominator
        return self

    def __imul__(self, other):
        result = self * other
        self.numerator = result.numerator
        self.denominator = result.denominator
        return self

    def __idiv__(self, other):
        result = self / other
        self.numerator = result.numerator
        self.denominator = result.denominator
        return self

    def __int__(self):
        return self.numerator // self.denominator

    def __float__(self):
        return float(self.numerator) / float(self.denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

print(fraction1 + fraction2)
print(fraction1 - fraction2)
print(fraction1 * fraction2)
print(fraction1 / fraction2)

print(Fraction(1, 3))
print(Fraction(1, 6))
print(Fraction(2, 3))
print(Fraction(5, 6))

print(int(fraction1))
print(float(fraction1))
print(str(fraction1))


# Задание 2
class Airplane:
    def __init__(self, type, max_pas):
        self.type = type
        self.max_pas = max_pas
        self.current_pas = 0

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.type == other.type
        return False

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.max_pas > other.max_pas
        return False

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.max_pas < other.max_pas
        return False

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.max_pas <= other.max_pas
        return False

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.max_pas >= other.max_pas
        return False

    def __add__(self, other):
        if isinstance(other, int):
            if self.current_pas + other <= self.max_pas:
                self.current_pas += other
            else:
                raise ValueError(
                    'Максимальное количество пассажиров')
        return self

    def __sub__(self, other):
        if isinstance(other, int):
            if self.current_pas - other >= 0:
                self.current_pas -= other
            else:
                raise ValueError(
                    'Не может быть отрицательным')
        return self

    def __iadd__(self, other):
        if isinstance(other, int):
            if self.current_pas + other <= self.max_pas:
                self.current_pas += other
            else:
                raise ValueError(
                    'Максимальное количество пассажиров')
        return self

    def __isub__(self, other):
        if isinstance(other, int):
            if self.current_pas - other >= 0:
                self.current_pas -= other
            else:
                raise ValueError(
                    'Не может быть отрицательным')
        return self


plane1 = Airplane('Boeing 747', 420)
plane2 = Airplane('Airbus A380', 850)
plane3 = Airplane('Boeing 737', 230)

print(plane1 == plane3)
print(plane2 > plane1)

plane1 += 420
plane2 += 10
print(f'Количество пассажиров в {plane1.type}: {plane1.current_pas}')
print(f'Количество пассажиров в {plane2.type}: {plane2.current_pas}')


# Задание 3
class Flat:
    def __init__(self, square, price):
        self.square = square
        self.price = price

    # @staticmethod
    # def extract(string):
    #     result = ''
    #     temp = ''
    #     if isinstance(string, str):
    #         for i in string:
    #             if i.isdigit():
    #                 temp += str(i)
    #             elif i.isalpha() and len(temp) != 0:
    #                 if len(temp) != 0:
    #                     result, temp = temp, ''
    #         if len(temp) != 0 and len(result) == 0:
    #             result, temp = temp, ''
    #         if len(result) > 0 and len(temp) > 0:
    #             raise TypeError("Unsupported operand type")
    #         if len(result) != 0:
    #             return int(result)
    #     return 0

    def __eq__(self, other):  # ==
        if isinstance(other, Flat):
            return self.square == other.square
        elif isinstance(other, (int, float)):
            return self.square == other
        else:
            raise TypeError('Unsupported operand type')

    def __ne__(self, other):  # !=
        if isinstance(other, Flat):
            return self.square != other.square
        elif isinstance(other, (int, float)):
            return self.square != other
        else:
            raise TypeError('Unsupported operand type')

    def __lt__(self, other):  # <
        if isinstance(other, Flat):
            return self.price < other.price
        elif isinstance(other, (int, float)):
            return self.price < other
        else:
            raise TypeError('Unsupported operand type')

    def __gt__(self, other):  # >
        if isinstance(other, Flat):
            return self.price > other.price
        elif isinstance(other, (int, float)):
            return self.price > other
        else:
            raise TypeError('Unsupported operand type')

    def __le__(self, other):  # <=
        if isinstance(other, Flat):
            return self.price <= other.price
        elif isinstance(other, (int, float)):
            return self.price <= other
        else:
            raise TypeError('Unsupported operand type')

    def __ge__(self, other):  # >=
        if isinstance(other, Flat):
            return self.price >= other.price
        elif isinstance(other, (int, float)):
            return self.price >= other
        else:
            raise TypeError('Unsupported operand type')


flat1 = Flat(100, 50000)
flat2 = Flat(120, 60000)
flat3 = Flat(100, 55000)

print(flat1 == flat3)
print(flat1 != flat2)
print(flat2 > flat1)
print(flat1 < flat3)
print(flat1 <= flat3)
print(flat2 >= flat3)


# Задание 4
class Operation:
    def perform(self, operand1, operand2):
        pass


class Addition(Operation):
    def perform(self, operand1, operand2):
        return operand1 + operand2


class Subtraction(Operation):
    def perform(self, operand1, operand2):
        return operand1 - operand2


class Multiplication(Operation):
    def perform(self, operand1, operand2):
        return operand1 * operand2


class Division(Operation):
    def perform(self, operand1, operand2):
        if operand2 == 0:
            return 'Division by zero'
        return operand1 / operand2


class Calculator:
    def calculate(self, operand1, operand2, operation):
        return operation.perform(operand1, operand2)


addition = Addition()
subtraction = Subtraction()
multiplication = Multiplication()
division = Division()
calculator = Calculator()

print(calculator.calculate(5, 3, addition))
print(calculator.calculate(10, 4, subtraction))
print(calculator.calculate(6, 7, multiplication))
print(calculator.calculate(8, 2, division))



# test
# class Test:
#     def __init__(self, a, b):
#         if isinstance(a, str):
#             self.a = self.__extract(a)
#         else:
#             self.a = a
#         if isinstance(b, str):
#             self.b = self.__extract(b)
#         else:
#             self.b = b
#
#     @classmethod
#     def __extract(cls, string):
#         result = ''
#         temp = ''
#         if isinstance(string, str):
#             for i in string:
#                 if i.isdigit():
#                     temp += str(i)
#                 elif i.isalpha() and len(temp) != 0:
#                     if len(temp) != 0:
#                         result, temp = temp, ''
#             if len(temp) != 0 and len(result) == 0:
#                 result, temp = temp, ''
#             if len(result) > 0 and len(temp) > 0:
#                 raise TypeError("Unsupported operand type")
#             if len(result) != 0:
#                 return int(result)
#         return 0
#
#     def show_info(self):
#         print(type(self.a))
#         print(self.a)
#         print(type(self.b))
#         print(self.b)
#
#
# c = Test('aaa10', 'hgh20jk')
# c.show_info()
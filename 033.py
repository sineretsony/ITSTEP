# import logging
#
# logging.basicConfig(level=logging.DEBUG, filename='logs.log', filemode='w',
#                     format='loggin message: %(asctime)s:%(levelname)s - %(message)s')
#
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')
#
# try:
#     print(10 / 0)
# except Exception as ex:
#     logging.exception(ex)
#     logging.error(ex)

# def adder(*args, **kwargs):
#     result = 0
#     for value in args:
#         if type(value) == int or type(value) == float or type(value) == bool:
#             result += value
#         else:
#             try:
#                 result += float(value)
#                 continue
#             except (ValueError, TypeError):
#                 pass
#             try:
#                 result += int(value)
#                 continue
#             except (ValueError, TypeError):
#                 pass
#
#     for value in kwargs.values():
#         if type(value) == int or type(value) == float or type(value) == bool:
#             result += value
#         else:
#             try:
#                 result += float(value)
#                 continue
#             except (ValueError, TypeError):
#                 pass
#             try:
#                 result += int(value)
#                 continue
#             except (ValueError, TypeError):
#                 pass
#
#     return result


# import unittest
# import test
#
#
# class MyTest(unittest.TestCase):
#     def test_args(self):
#         self.assertEqual(test.adder(2, 2), 4)
#
#     def test_kwargs(self):
#         self.assertEqual(test.adder(a=1, x=2), 3)
#
#     def test_mixed(self):
#         self.assertEqual(test.adder(1, x=2), 3)
#
#     def test_diff(self):
#         x = 10
#         y = 0
#         self.assertEqual(test.adder(0, -5, y, a=x), 5)
#
#     def test_wrong_type(self):
#         self.assertEqual(test.adder('5', 'abc', 10, True), 16)
#
#     def test_list(self):
#         nums = [1, 2, 3, 5]
#         self.assertEqual(test.adder(nums), 11)


import unittest
import test


def calculate_average(numbers):
    if type(numbers) == list and len(numbers) != 0:
        return sum(numbers) / len(numbers)
    else:
        return None


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

    def exponentiate(self, base, exponent):
        return base ** exponent

    def factorial(self, n):
        if n < 0:
            raise ValueError
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result



import unittest
# import average_calculator_033


# def calculate_average(numbers):
#     if type(numbers) == list and len(numbers) != 0:
#         return sum(numbers) / len(numbers)
#     else:
#         return None
#
#
# class MyTest(unittest.TestCase):
#     def test_average(self):
#         self.assertEqual(average_calculator_033.calculate_average([2, 2, 2]), 2)
#         self.assertEqual(average_calculator_033.calculate_average([1, 1.5, 5, -10, 20]), 3.5)
#
#     def test_empty_list(self):
#         self.assertEqual(average_calculator_033.calculate_average([]),None)
#
#     def test_one_dig(self):
#         self.assertEqual(average_calculator_033.calculate_average([2]), 2)
#
#     def test_negative_number(self):
#         self.assertEqual(average_calculator_033.calculate_average([-2, -2, -2]), -2)
#
#     def test_mixed_numbers(self):
#         self.assertEqual(average_calculator_033.calculate_average([1, 2, 3, 4, 5]), 3.0)
#         self.assertEqual(average_calculator_033.calculate_average([-1, 0, 1]),0.0)
#
#     def test_non_list_input(self):
#         self.assertEqual(average_calculator_033.calculate_average(42), None)
#         self.assertEqual(average_calculator_033.calculate_average("not list"), None)
#
#     def test_large_numbers(self):
#         numbers = list(range(1, 10001))
#         self.assertEqual(average_calculator_033.calculate_average(numbers),5000.5)
#
#     def test_float_numbers(self):
#         self.assertEqual(average_calculator_033.calculate_average([1.0, 2.0, 3.0]), 2.0)

# class Calculator:
#     def add(self, a, b):
#         return a + b
#
#     def subtract(self, a, b):
#         return a - b
#
#     def multiply(self, a, b):
#         return a * b
#
#     def divide(self, a, b):
#         if b == 0:
#             raise ValueError("Division by zero")
#         return a / b
#
#     def exponentiate(self, base, exponent):
#         return base ** exponent
#
#     def factorial(self, n):
#         if n < 0:
#             raise ValueError
#         if n == 0:
#             return 1
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result

# class MyTest2(unittest.TestCase):
#     def test_addition(self):
#         calc = average_calculator_033.Calculator()
#         result = calc.add(5, 3)
#         self.assertEqual(result, 8)
#
#     def test_subtraction(self):
#         calc = average_calculator_033.Calculator()
#         result = calc.subtract(5, 3)
#         self.assertEqual(result, 2)
#
#     def test_multiplication(self):
#         calc = average_calculator_033.Calculator()
#         result = calc.multiply(5, 3)
#         self.assertEqual(result, 15)
#
#     def test_division(self):
#         calc = average_calculator_033.Calculator()
#         result = calc.divide(6, 3)
#         self.assertEqual(result, 2.0)
#
#     def test_division_by_zero(self):
#         calc = average_calculator_033.Calculator()
#         with self.assertRaises(ValueError):
#             calc.divide(6, 0)
#
#     def test_exponentiation(self):
#         calc = average_calculator_033.Calculator()
#         result = calc.exponentiate(2, 3)
#         self.assertEqual(result, 8)
#
#     def test_exponentiation_zero(self):
#         calc = average_calculator_033.Calculator()
#         result = calc.exponentiate(5, 0)
#         self.assertEqual(result, 1)
#
#     def test_factorial(self):
#         calc = average_calculator_033.Calculator()
#         result = calc.factorial(5)
#         self.assertEqual(result, 120)
#
#     def test_factorial_of_zero(self):
#         calc = average_calculator_033.Calculator()
#         result = calc.factorial(0)
#         self.assertEqual(result, 1)
#
#     def test_factorial_of_negative(self):
#         calc = average_calculator_033.Calculator()
#         with self.assertRaises(ValueError):
#             calc.factorial(-5)
#
#     def test_non_int_factorial(self):
#         calc = average_calculator_033.Calculator()
#         with self.assertRaises(TypeError):
#             calc.factorial(5.5)



































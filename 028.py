# class Animal:
#     def __init__(self, name, age, color):
#         print("init of base class")
#         self.__name = name
#         self.__age = age
#         self.__color = color
#
#     def show_info(self):
#         print(f"Имя {self.__name},\nВозраст {self.__age},\nЦвет {self.__color}")
#
#     def golos(self):
#         print("golos")
#
#
# class Cat(Animal):
#     def __init__(self, name, age, color, hp=9):
#         print("init of cat class")
#         super().__init__(name, age, color)
#         self.hp = hp
#
#     def show_info(self):
#         super().show_info()
#         print(f'hp: {self.hp}')
#
#     def golos(self):
#         print("may")
#
#
# class Dog(Animal):
#     def __init__(self, name, age, color):
#         print("init of cat class")
#         super().__init__(name, age, color)
#
#     def golos(self):
#         print("gof")
#
#
# class Cow(Animal):
#     def __init__(self, name, age, color):
#         print("init of cat class")
#         super().__init__(name, age, color)
#
#     def golos(self):
#         print("myy")
#
#
# cat1 = Cat("Мурка", 5, "серый")
# cat1.show_info()
#
# myDog = Dog('sharik', 6, 'balck')
# myDog.golos()
#
# import random
#
#
# class Person:
#     def __init__(self, first_name, last_name, age):
#         # public prop
#         self.first_name = first_name
#         self.last_name = last_name
#         # protected prop
#         self._age = age
#
#         # private prop
#         self.__id = random.randint(0, 100)
#
#     def __show_id(self):
#         return self.__id
#
#     def get_info(self):
#         return (f'Name: {self.first_name} {self.last_name},'
#                 f'\nage: {self._age},\nid: {self.__show_id()}')
#
#
# person = Person('Bill', 'Geits', 50)
# print(person.get_info())
#
#
# class Employee(Person):
#     def __init__(self, first_name, last_name, age, salary):
#         super().__init__(first_name, last_name, age)
#         self.__salary = salary
#
#     def set_age(self, mew_age):
#         self._age = mew_age
#
#     def isRetire(self):
#         print(self.get_info())
#         if self._age > 65:
#             print(f'{self.last_name} is retire')
#         else:
#             print(f'{self.last_name} is not retire')
#
#     @staticmethod
#     def testFunc():
#         print('test')
#
#     @staticmethod
#     def testFunc2():
#         print('test2')
#
#
# employee = Employee('Bill', 'Gates', 65, 1000000)
# print(employee.get_info())
#
# worker = Employee('Han', 'Solo', 39, 500)
# print('-----------------------------------')
# worker.isRetire()
# worker.set_age(70)
# worker.isRetire()


# class Dates:
#     def __init__(self, date):
#         self.date = date
#
#     def __del__(self):
#         print(f'Deleting Dates object with date: {self.date}')
#
#     def get_date(self):
#         return self.date
#
#     @staticmethod
#     def toDashDate(date):
#         return date.replace('/', "-")
#
#
# dateFromdb = Dates('13/10/2023')
# dateWithDash = Dates.toDashDate(dateFromdb.get_date())
# print(dateWithDash)
#
#
# class DatesShis(Dates):
#     def get_date(self):
#         return Dates.toDashDate(self.date)
#
#
# newDate = DatesShis('13/10/2023')
# print(newDate.get_date())


# Задание 1

class Figure:
    def __init__(self, color, pi, x, y):
        self.color = color
        self.pi = pi
        self.x = x
        self.y = y

    def show_info(self):
        print("Цвет:", self.color)
        print("Число Пи:", self.pi)
        print("Координаты:", self.x, self.y)

    def fill(self, color):
        self.color = color


class Triangle(Figure):
    def __init__(self, color, pi, x1, y1, x2, y2, x3, y3):
        super().__init__(color, pi, (x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3)
        self.x1, self.y1, self.x2, self.y2, self.x3, self.y3 = x1, y1, x2, y2, x3, y3

    def area(self):
        return 0.5 * self.pi * (self.x1 * (self.y2 - self.y3)
                                + self.x2 * (self.y3 - self.y1)
                                + self.x3 * (self.y1 - self.y2))


class Circle(Figure):
    def __init__(self, color, pi, x, y, r):
        super().__init__(color, pi, x, y)
        self.r = r

    def area(self):
        return self.pi * self.r ** 2


class Rectangle(Figure):
    def __init__(self, color, pi, x, y, w, h):
        super().__init__(color, pi, x, y)
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


triangle = Triangle("red", 3.14, 0, 0, 10, 0, 5, 10)
triangle.show_info()
print("Площадь треугольника:", triangle.area())
print('----------------------------------')

circle = Circle("blue", 3.14, 0, 0, 5)
circle.show_info()
print("Площадь круга:", circle.area())
print('----------------------------------')
rectangle = Rectangle("green", 3.14, 0, 0, 10, 20)
rectangle.show_info()
print("Площадь прямоугольника:", rectangle.area())

# Задание 2

import random


class Person:
    count_obj = 0

    def __init__(self, first_name, last_name, age):
        # public prop
        self.first_name = first_name
        self.last_name = last_name
        # protected prop
        self._age = age

        # private prop
        self.__id = random.randint(0, 100)
        Person.count_obj += 1

    def __show_id(self):
        return self.__id

    def get_info(self):
        return (f'Name: {self.first_name} {self.last_name},'
                f'\nage: {self._age},\nid: {self.__show_id()}')

    @staticmethod
    def count_class():
        return Person.count_obj


person = Person('Bill', 'Geits', 50)
print(person.get_info())

person2 = Person('Tom', 'land', 25)
print(person2.get_info())

count = Person.count_class()
print('Кол-во вызовов: ', count)


# Задание 3
class Passport:
    def __init__(self, first_name, last_name, id, country):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.country = country

    def show_info(self):
        return (f'Имя и Фамилия: {self.first_name}, {self.last_name}\n'
                f'Номер паспорта: {self.id}\n'
                f'Страна: {self.country}')


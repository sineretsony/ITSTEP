# import random
# from datetime import datetime
#
#
# class Person:
#     count_obj = 0
#     hobby = 'cooking'
#     personAge = 0
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self._age = age
#         self.__id = random.randint(0, 100)
#         Person.count_obj += 1
#
#     def __show_id(self):
#         return self.__id
#
#     def get_info(self):
#         return (f'Name: {self.first_name} {self.last_name},'
#                 f'\nage: {self._age},\nid: {self.__show_id()}\n'
#                 f'Hobby: {self.hobby}')
#
#     @staticmethod
#     def count_class():
#         return Person.count_obj
#
#     @classmethod
#     def count_class2(cls):
#         return cls.count_obj
#
#     @classmethod
#     def set_hobby(cls, new_hobby):
#         cls.hobby = new_hobby
#
#     @classmethod
#     def based(cls, firstName, lastname, year):
#         personAge = datetime.today().year - year
#         return cls(firstName, lastname, personAge)
#
#     @classmethod
#     def basedOnStr(cls, name_str):
#         first_name, last_name, b_year = name_str.split()
#         b_year = int(b_year)
#
#         c_year = datetime.today().year
#         personAge = c_year - b_year
#         return cls(first_name, last_name, personAge)
#
#
# person = Person('Bill', 'Gates', 1955)
# print(person.get_info())
#
# person2 = Person('Tom', 'Land', 1998)
# Person.set_hobby('drawing')
# print(person2.get_info())
#
# count = Person.count_class()
# print('Кол-во вызовов:', count)
#
# person_str = 'John Doe 1985'
# person_from_str = Person.basedOnStr(person_str)
# print(person_from_str.get_info())
#
# print(Person.count_class2())

# class MyBook:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def showInfo(self):
#         print(f'Title: {self.title}\n'
#               f'Author: {self.author}\n'
#               f'Pages: {self.pages}')
#
#
# class MyFile:
#     def __init__(self, file_size, src):
#         self.file_size = file_size
#         self.src = src
#
#     def showInfo(self):
#         print(f"File size: {self.file_size}\n"
#               f"SRC: {self.src}")
#
#
# class MyEBook(MyBook, MyFile):
#     def __init__(self, title, author, pages, file_size, src):
#         MyBook.__init__(self, title, author, pages)
#         MyFile.__init__(self, file_size, src)
#
#     def showInfo(self):
#         MyBook.showInfo(self)
#         MyFile.showInfo(self)
#
#
# # линеаризация класса, порядок имён задаёт порядок вызовов MRO
# ebook = MyEBook('Python', 'Gvido', 333, 1024, 'https://dsisdd.com')
# ebook.showInfo()
#
# print(MyEBook.mro())


# class MyClass1:
#     def sayHi(self):
#         print('Hi from class 1')
#
#
# class MyClass2(MyClass1):
#     def sayHi(self):
#         print('Hi from class 2')
#
#
# class MyClass3(MyClass1):
#     def sayHi(self):
#         print('Hi from class 3')
#
#
# class MyClass4(MyClass2, MyClass3):
#     pass
#
#
# myObj = MyClass4()
# myObj.sayHi()
#
# print(MyClass4.mro())
# Задание 1
# class Brain:
#     def __init__(self, weight):
#         self.weight = weight
#
#     def show_info(self):
#         print(f'Вес мозга: {self.weight}')
# class Heart:
#     def __init__(self, power):
#         self.power = power
#
#     def show_info(self):
#         print(f'Мощность сердца: {self.power}')
# class Lungs:
#     def __init__(self, capacity):
#         self.capacity = capacity
#
#     def show_info(self):
#         print(f'Объём лёгких: {self.capacity}')
# class Stomach:
#     def __init__(self, capacity_stomach):
#         self.capacity_stomach = capacity_stomach
#
#     def show_info(self):
#         print(f"Объем желудка: {self.capacity_stomach}")
# class Arms:
#     def __init__(self, strength):
#         self.strength = strength
#
#     def show_info(self):
#         print(f"Сила руки: {self.strength}")
# class Legs:
#     def __init__(self, muscle_mass):
#         self.muscle_mass = muscle_mass
#
#     def show_info(self):
#         print(f"Мышечная масса ног: {self.muscle_mass}")
#
# class Human(Brain, Heart, Lungs, Stomach, Arms, Legs):
#     def __init__(self, weight, power, capacity, capacity_stomach,
#                  strength, muscle_mass):
#         Brain.__init__(self, weight)
#         Heart.__init__(self, power)
#         Lungs.__init__(self, capacity)
#         Stomach.__init__(self, capacity_stomach)
#         Arms.__init__(self, strength)
#         Legs.__init__(self, muscle_mass)
#
#     def show_info(self):
#         Brain.show_info(self)
#         Heart.show_info(self)
#         Lungs.show_info(self)
#         Stomach.show_info(self)
#         Arms.show_info(self)
#         Legs.show_info(self)
#
#
# my_first_human = Human(2000, '4500', 7, 2, 4.5, 8)
# my_first_human.show_info()


class Instrument:
    def play(self):
        print("Игра на инструменте")


class StringInstrument(Instrument):
    def play(self):
        print("Игра на струнном инструменте")


class WindInstrument(Instrument):
    def play(self):
        print("Игра на Духовом инструменте")


class PercussionInstrument(Instrument):
    def play(self):
        print("Игра на ударном инструменте")


class Guitar(StringInstrument):
    def play(self):
        print("Игра на гитаре")


class Flute(WindInstrument):
    def play(self):
        print("Игра на флейте")


class Drum(PercussionInstrument):
    def play(self):
        print("Игра на Drum")


class HybridInstrument(StringInstrument, WindInstrument, PercussionInstrument):
    def play(self):
        print("Игра на гибридном инструменте")
        StringInstrument.play(self)
        WindInstrument.play(self)
        PercussionInstrument.play(self)


def show_info(instrument):
    instrument.play()


guitar = Guitar()
flute = Flute()
drum = Drum()
print("Игра на гитаре:")
show_info(guitar)
print("Игра на флейте:")
show_info(flute)
print("Игра на ударном инструменте:")
show_info(drum)
hybrid_instrument = HybridInstrument()
print("Игра на гибридном инструменте:")
show_info(hybrid_instrument)

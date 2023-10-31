# class Human:
#     __slots__ = ('name', 'gender', 'age')
#
#     def __init__(self):
#         self.name = 'human'
#
#
# human = Human()
# human.age = 30
# print(human.name)
# print(human.age)
#
#
# # print(human.__dict__)
#
# class Student(Human):
#     __slots__ = ('__marks',)
#
#     def __init__(self):
#         super().__init__()
#         self.__marks = []
#
#     def showInfo(self):
#         print(f'name : {self.name}, {self.__marks}')
#
#
# st = Student()
# # st.mood = 'good'
# st.showInfo()
# # print(st.mood)
# st.age = 18
# print(st.age)

from abc import ABC, abstractmethod, abstractproperty
import random


# class AbstractBaseClass(ABC):
#     def test(self):
#         print('test')
#
#     @abstractmethod
#     def show_abc(self):
#         pass
#
#
# class testBase(AbstractBaseClass):
#     def test2(self):
#         print('test2')
#
#     def show_abc(self):
#         print('test2_2')
#
#
# # abc = AbstractBaseClass()
# # abc.show_abc()
#
# test = testBase()
# test.test2()
# test.show_abc()
#
# class A

# class AbstractBasePlayer(ABC):
#     def __init__(self, name, rasa):
#         self.name = name
#         self.rasa = rasa
#
#     def show_info(self):
#         print(f'name: {self.name}, rasa: {self.rasa}')
#
#     @abstractmethod
#     def attack(self):
#         pass
#
#
# class Human(AbstractBasePlayer):
#     def __init__(self, name, age):
#         super().__init__(name, 'human')
#         self.age = age
#
#     def attack(self):
#         print(f'{self.rasa} attack sword!')
#
#     def show_info(self):
#         super().show_info()
#         print(f'age {self.age}')
#
#
# class Elf(AbstractBasePlayer):
#     def __init__(self, name, age):
#         super().__init__(name, 'elf')
#         self.age = age
#
#     def attack(self):
#         print(f'{self.rasa} attack bow!')
#
#     def show_info(self):
#         super().show_info()
#         print(f'age {self.age}')
#
#
# class Dwarf(AbstractBasePlayer):
#     def __init__(self, name, age):
#         super().__init__(name, 'dwarf')
#         self.age = age
#
#     def attack(self):
#         print(f'{self.rasa} attack hammer!')
#
#     def show_info(self):
#         super().show_info()
#         print(f'age {self.age}')


# human.show_info()
# human.attack()


# elf.show_info()
# elf.attack()


# dwarf.show_info()
# dwarf.attack()

#
# class Game:
#     def __init__(self):
#         self.players = []
#
#     def add_player(self, *args):
#         for new_player in args:
#             if isinstance(new_player, AbstractBasePlayer):
#                 self.players.append(new_player)
#             else:
#                 print('Error type of new player')
#
#     def show_players(self):
#         if self.players:
#             for player in self.players:
#                 player.show_info()
#         else:
#             print('Zero players!')
#
#     def fight(self):
#         player1 = random.choice(self.players)
#         player2 = random.choice(self.players)
#         while player1 == player2:
#             player2 = random.choice(self.players)
#         player1.attack()
#         player2.attack()
#
#
# human = Human('Persey', 50)
# elf = Elf('Appoly', 900)
# dwarf = Dwarf('Borvik', 90)
#
# game = Game()
# game.add_player(human, elf, dwarf)
# game.show_players()
# game.fight()


# class Pets(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
#
#     @abstractmethod
#     def show(self):
#         pass
#
#     @abstractmethod
#     def type(self):
#         pass
#
#
# class Dog(Pets):
#     def __init__(self, name):
#         self.name = name
#
#     def sound(self):
#         print('gow gow')
#
#     def show(self):
#         print(f'name: {self.name}')
#
#     def type(self):
#         print('Canis familiaris')
#
#
# class Cat(Pets):
#     def __init__(self, name):
#         self.name = name
#
#     def sound(self):
#         print('may may')
#
#     def show(self):
#         print(f'name: {self.name}')
#
#     def type(self):
#         print('Felis silvestris')
#
#
# my_dog = Dog('Tiff')
# my_dog.sound()
# my_dog.show()
# my_dog.type()
#
# my_cat = Cat('Myrka')
# my_cat.sound()
# my_cat.show()
# my_cat.type()

# class Zoo:
#     __slots__ = ('animals',)
#
#     def __init__(self):
#         self.animals = []
#
#     def add_animal(self, animal):
#         self.animals.append(animal)
#         print(f'{animal.name} добавлен в зоопарк.')
#
#     def remove_animal(self, animal):
#         if animal in self.animals:
#             self.animals.remove(animal)
#             print(f"{animal.name} переехал")
#         else:
#             print(f'{animal.name} нет в зоопарке')
#
#     def list_animals(self):
#         print('Животные в зоопарке:')
#         for animal in self.animals:
#             print(f"{animal.name}: {animal.species}")
#
#
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#
#
# zoo = Zoo()
#
# lion = Animal("Simba", "Lion")
# tiger = Animal("Tony", "Tiger")
# elephant = Animal("Dumbo", "Elephant")
#
# zoo.add_animal(lion)
# zoo.add_animal(tiger)
# zoo.add_animal(elephant)
# zoo.list_animals()
# zoo.remove_animal(lion)
# zoo.list_animals()

class Ship(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def fire(self, target):
        pass

    @abstractmethod
    def move(self, end):
        pass


class Battleship(Ship):
    def __init__(self, name):
        self.name = name
        self.length = 1

    def fire(self, target):
        print(f"{self.name} атакует {target}")

    def move(self, end):
        print(f"{self.name} перемещается {end}")

    def __str__(self):
        return f'{self.name}'


class Submarine(Ship):
    def __init__(self, name):
        self.name = name
        self.length = 1

    def fire(self, target):
        print(f"{self.name} атакует {target}.")

    def move(self, end):
        print(f"{self.name} перемещается {end}")

    def __str__(self):
        return f'{self.name}'


class Player:
    def __init__(self, name):
        self.name = name
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)

    def show_info(self):
        for s in self.ships:
            print(s.name)


class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def play(self):
        while True:
            for p in self.players:
                print(f"{p.name}'ходит:")
                target_player = p
                while target_player == p:
                    target_player = random.choice(self.players)

                attack_ship = random.choice(p.ships)
                target_ship = random.choice(target_player.ships)

                attack_ship.fire(target_ship)

                if random.random() < 0.5:
                    print(f"{attack_ship.name} попал в {target_ship.name}!")
                    target_player.ships.remove(target_ship)
                else:
                    print(f"{attack_ship.name} промахнулся!")

                if not target_player.ships:
                    print(f"{p.name} выиграл игру!")
                    return


player1 = Player("Игрок 1")
player2 = Player("Игрок 2")

player1.add_ship(Battleship("Линкор 1"))
player1.add_ship(Battleship("Линкор 3"))
player1.add_ship(Submarine("Подводная лодка 1"))
player2.add_ship(Battleship("Линкор 2"))
player2.add_ship(Battleship("Линкор 4"))
player2.add_ship(Submarine("Подводная лодка 2"))

game = Game()
game.add_player(player1)
game.add_player(player2)
game.play()

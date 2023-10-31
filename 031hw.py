# Задание 1
import sys
from abc import ABC, abstractmethod, abstractproperty
import random




class Contact:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def __str__(self):
        return (f'First name: {self.first_name}\n'
                f'Last name: {self.last_name}\n'
                f'email: {self.email}\n'
                f'Phone number: {self.phone_number}')


class OptimizedContact:
    __slots__ = ('first_name', 'last_name', 'email', 'phone_number')

    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def __str__(self):
        return (f'First name: {self.first_name}\n'
                f'Last name: {self.last_name}\n'
                f'email: {self.email}\n'
                f'Phone number: {self.phone_number}')


con1 = Contact('Gregoire', 'Gorea', 'gorea@email.com', '+38000000000')
con2 = Contact('Sergiy', 'Vasilevskiy', 'vasilev@email.com', '+38000000000')
print(sys.getsizeof(con1))
print(sys.getsizeof(con2))

con3 = OptimizedContact('Gregoire', 'Gorea', 'gorea@email.com', '+38000000000')
con4 = OptimizedContact('Sergiy', 'Vasilevskiy', 'vasilev@email.com', '+38000000000')
print(sys.getsizeof(con3))
print(sys.getsizeof(con4))

'''Использование __slots__ не всегда приводит к уменьшению потребления памяти.
Он ограничивает набор атрибутов, которые могут быть созданы для каждого объекта,
что может быть полезно в определенных случаях, но при этом может увеличить объем памяти,
занимаемый самим классом и некоторыми дополнительными структурами данных.'''

# Задание 2
class Ship(ABC):

    @abstractmethod
    def __init__(self, name):
        pass

    @abstractmethod
    def fire(self, target):
        pass

    @abstractmethod
    def up_armor(self):
        pass

    @abstractmethod
    def up_attack(self):
        pass

    @abstractmethod
    @property
    def hp(self):
        pass

    @abstractmethod
    @hp.setter
    def hp(self, new_hp):
        pass

    @abstractmethod
    @property
    def maneuver(self):
        pass

    @abstractmethod
    @maneuver.setter
    def maneuver(self, value=0):
        pass

    @abstractmethod
    @property
    def attack(self):
        pass

    @abstractmethod
    @property
    def armor(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Battleship(Ship):
    __slots__ = ('name', 'hp_ship', 'attack_ship', 'armor_ship', 'evasion')

    def __init__(self, name):
        self.name = name
        self.hp_ship = 270
        self.attack_ship = 80
        self.armor_ship = 40
        self.evasion = 0

    def fire(self, target):
        print(f"{self.name} атакует {target}")
        return self.attack_ship

    def up_armor(self):
        print('Броня улучшена на +5')
        self.armor_ship += 5

    def up_attack(self):
        print('Атака улучшена на +10')
        self.attack_ship += 10

    @property
    def hp(self):
        return self.hp_ship

    @hp.setter
    def hp(self, new_hp):
        self.hp_ship = new_hp

    @property
    def maneuver(self):
        return self.evasion

    @maneuver.setter
    def maneuver(self, value=0):
        self.evasion = value

    @property
    def attack(self):
        return self.attack_ship

    @property
    def armor(self):
        return self.armor_ship

    def __str__(self):
        return f'{self.name}'


class Submarine(Ship):
    __slots__ = ('name', 'hp_ship', 'attack_ship', 'armor_ship', 'evasion')

    def __init__(self, name):
        self.name = name
        self.hp_ship = 170
        self.attack_ship = 80
        self.armor_ship = 40
        self.evasion = 0

    def fire(self, target):
        print(f"{self.name} атакует {target}")
        return self.attack_ship

    def up_armor(self):
        print('Броня улучшена на +5')
        self.armor_ship += 5

    def up_attack(self):
        print('Атака улучшена на +10')
        self.attack_ship += 10

    @property
    def hp(self):
        return self.hp_ship

    @hp.setter
    def hp(self, new_hp):
        self.hp_ship = new_hp

    @property
    def maneuver(self):
        return self.evasion

    @maneuver.setter
    def maneuver(self, value=0):
        self.evasion = value

    @property
    def attack(self):
        return self.attack_ship

    @property
    def armor(self):
        return self.armor_ship

    def __str__(self):
        return f'{self.name}'


class Player:
    def __init__(self, name):
        self.name = name
        self.ships = []
        self.money_player = 1000

    def add_ship(self, ship):
        if len(self.ships) < 4:
            self.ships.append(ship)
        else:
            print("Нельзя добавить больше 4 кораблей")

    def remove_ship(self, name):
        self.ships.remove(name)

    def show_ships(self):
        return self.ships

    @property
    def money(self):
        return self.money_player

    @money.setter
    def money(self, n):
        self.money_player = n


class Game:
    def __init__(self):
        self.players = [Player('Capitan Bot')]
        self.ships = [Battleship("Линк Аркана"), Battleship("Линкор Дредноут"),
                      Battleship("Линк Фурия"), Battleship("Линкор Тиран"),
                      Submarine("Субм Морская Звезда"),
                      Submarine("Субм Акула"),
                      Submarine("Субм Молния"), Submarine("Субм Бурильщик")]

    def __initialize_bot(self):
        bot = self.players[0]
        for i in [0, 2, 7, 5]:
            bot.add_ship(self.ships[i])

    def __initialize_player(self):
        player = self.players[1]
        for i in [1, 3, 6, 4]:
            player.add_ship(self.ships[i])

    def __add_player(self, name):
        player = Player(name)
        self.players.append(player)

    def __calc_damage(self, a, ar):
        if ar > a:
            return 0
        return a - ar

    def __vin(self, name):
        print(f'Игрок {name} победил')

    def __update(self):
        while True:
            print(f'Монет: {self.players[1].money_player}')
            for i, ship in enumerate(self.players[1].show_ships()):
                print(f'{i + 1}, {ship.name}')
            ship_update = int(
                input('Выберите корабль для улучшения (или 0 для выхода): '))
            if ship_update == 0:
                break
            if 0 <= ship_update - 1 < len(self.players[1].ships):
                ship = self.players[1].ships[ship_update - 1]
                cost = 500
                if self.players[1].money >= cost:
                    self.players[1].money -= cost
                    ship.up_armor()
                    ship.up_attack()
                    print(f'Корабль {ship.name} улучшен!')
                    print(f'Характеристики:\n'
                          f'Атака: {ship.attack}\n'
                          f'Броня: {ship.armor}')
                else:
                    print('У вас недостаточно монет для улучшения корабля.')
            else:
                print('Неверный выбор корабля.')

    def play(self):
        name = input('Введите свой ник в игре: ')
        self.__add_player(name)
        self.__initialize_bot()
        self.__initialize_player()
        count = 0
        atk_tar, tar_atk = 0, 1
        game_play = False
        while True:
            print('Запустить игру   = 1')
            print('Купить улучшения = 2')
            print('Закончить игру   = 0')
            game_choice = int(input('Введите действие: '))
            if game_choice == 1:
                game_play = True
                self.__add_player(name)
                self.__initialize_bot()
                self.__initialize_player()
            elif game_choice == 2:
                self.__update()
            elif game_choice == 0:
                break

            while game_play:
                player_atk = self.players[atk_tar]
                player_target = self.players[tar_atk]

                if len(player_target.show_ships()) == 0:
                    self.__vin(player_atk.name)
                    game_play = False
                    break

                print(f'Ход {count + 1}')
                print(f"Ход {player_atk.name}:")

                for ship in player_atk.show_ships():
                    if atk_tar == 0:
                        available_ships = [s for s in
                                           player_target.show_ships() if
                                           s.hp > 0]
                        if not available_ships:
                            self.__vin(player_atk.name)
                            game_play = False
                            break
                        ch_ship = random.choice(available_ships)
                    else:
                        choice_ship = int(input('Выберите цель: '))
                        available_ships = [s for s in
                                           player_target.show_ships() if
                                           s.hp > 0]
                        if not available_ships:
                            self.__vin(player_atk.name)
                            game_play = False
                            break
                        if 1 <= choice_ship <= len(available_ships):
                            ch_ship = player_target.show_ships()[
                                choice_ship - 1]
                        else:
                            print('Выбран случайный корабль')
                            ch_ship = random.choice(available_ships)

                    print(f'{ship.name} атакует {ch_ship}')
                    damage = self.__calc_damage(ship.attack, ch_ship.armor)

                    if random.randint(1, 10) > 3:
                        ch_ship.hp -= damage
                        print(f'{ship.name} наносит {damage} урона\n'
                              f'кораблю {ch_ship} осталось хп {ch_ship.hp}')
                    else:
                        print(f'{ship.name} промахнулся!')

                    if ch_ship.hp <= 0:
                        player_target.remove_ship(ch_ship)
                        print(f'Корабль {ch_ship} потоплен!')
                        player_atk.money += 150

                count += 1

                if atk_tar == 0:
                    atk_tar, tar_atk = 1, 0
                else:
                    atk_tar, tar_atk = 0, 1


game = Game()
game.play()

'''Игра "BatlShip2" представляет собой увлекательный текстовый квест, 
в котором игроки участвуют в сражении между кораблями. 
В игре доступны различные возможности, такие как улучшение кораблей, 
возможность начать бой заново, заработать деньги и потратить их на улучшения.

Однако следует отметить, что в игре присутствует некоторое количество ошибок и недоработок, 
так как для полноценной логики требуется больше времени и более тщательного планирования.

На данный момент не реализована функция маневрирования, 
которая позволила бы кораблю избегать попаданий в него на один ходу.

Абстрактный метод помог правлиьно оформить классы кораблей'''
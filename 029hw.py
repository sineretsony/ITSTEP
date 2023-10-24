# Задание 1
class UniqueID:
    next_id = 1

    @classmethod
    def generate_id(cls):
        unique_id = cls.next_id
        cls.next_id += 1
        return unique_id


instance1 = UniqueID()
instance2 = UniqueID()

id1 = instance1.generate_id()
id2 = instance2.generate_id()

print("Идентификатор для instance1:", id1)
print("Идентификатор для instance2:", id2)


# Задание 2
class Movie:
    info_film = {}

    def __init__(self, name_film, rating):
        self.name_film = name_film
        self.rating = rating
        Movie.info_film[self.name_film] = self.rating

    @classmethod
    def average_rating(cls):
        data = Movie.info_film
        ratings = [float(rating) for rating in data.values()]
        average = sum(ratings) / len(ratings)
        print(f'Средний рейтинг фильмов: {average}')

    @classmethod
    def all_rating(cls):
        data = Movie.info_film.values()
        print('Рейтинг всех фильмов: ', end=' ')
        for r in data:
            print(r, end=', ')
        print(end='\n')

    @classmethod
    def all_name(cls):
        data = Movie.info_film.keys()
        print('Названия всех фильмов: ', end=' ')
        for n in data:
            print(n, end=', ')
        print(end='\n')

    @classmethod
    def search_by_name(cls, name):
        data = Movie.info_film
        if name in data:
            print(f'Рейтинг фимльма: {name}: {data[name]}')
        else:
            print('В списке нет такого фильма')


tenet = Movie('Tenet', 6)
inception = Movie('Inception', 8)
Movie.average_rating()
Movie.all_rating()
Movie.all_name()
Movie.search_by_name("Tenet")
print()


# Задание 3
class Car_body:
    def __init__(self, type_car_body):
        self.type_car_body = type_car_body

    def show_info(self):
        print(f'Тип кузова: {self.type_car_body}')


class Suspension:
    def __init__(self, type_suspension, type_drive):
        self.type_suspension = type_suspension
        self.type_drive = type_drive

    def show_info(self):
        print(f'Тип подвески: {self.type_suspension}')
        print(f'Тип привода: {self.type_drive}')


class Wheels:
    def __init__(self, radius):
        self.radius = radius

    def show_info(self):
        print(f'Радиус колеса: {self.radius}')


class Engine:
    def __init__(self, engine_capacity, number_cylinders, type_fuel):
        self.engine_capacity = engine_capacity
        self.number_cylinders = number_cylinders
        self.type_fuel = type_fuel

    def show_info(self):
        print(f'Объём двигателя: {self.engine_capacity}')
        print(f'Кол-во цилиндров: {self.number_cylinders}')
        print(f'Тип топлива: {self.type_fuel}')


class Gear_box:
    def __init__(self, type_gearbox, number_gears):
        self.type_gearbox = type_gearbox
        self.number_gears = number_gears

    def show_info(self):
        print(f'Тип коробки передач: {self.type_gearbox}')
        print(f'Кол-во передач: {self.number_gears}')


class Brakes:
    def __init__(self, type_brakes):
        self.type_brakes = type_brakes

    def show_info(self):
        print(f'Тип Тормозов: {self.type_brakes}')


class Door:
    def __init__(self, mounting_type):
        self.mounting_type = mounting_type

    def show_info(self):
        print(f'Тип крепления дверей: {self.mounting_type}')


class Vehicle_interior:
    def __init__(self, type_interior):
        self.type_interior = type_interior

    def show_info(self):
        print(f'Салон: {self.type_interior}')


class Car(Car_body, Suspension, Wheels, Engine, Gear_box, Brakes, Door, Vehicle_interior):
    def __init__(self, name_car, model, color, type_car_body, type_suspension, type_drive, radius, engine_capacity,
                 number_cylinders, type_fuel,
                 type_gearbox, number_gears, type_brakes, mounting_type, type_interior):
        Car_body.__init__(self, type_car_body)
        Suspension.__init__(self, type_suspension, type_drive)
        Wheels.__init__(self, radius)
        Engine.__init__(self, engine_capacity, number_cylinders, type_fuel)
        Gear_box.__init__(self, type_gearbox, number_gears)
        Brakes.__init__(self, type_brakes)
        Door.__init__(self, mounting_type)
        Vehicle_interior.__init__(self, type_interior)
        self.name_car = name_car
        self.model = model
        self.color = color

    def show_info(self):
        print(f'Название: {self.name_car}')
        print(f'Модель: {self.model}')
        print(f'Цвет: {self.color}')
        Car_body.show_info(self)
        Suspension.show_info(self)
        Wheels.show_info(self)
        Engine.show_info(self)
        Gear_box.show_info(self)
        Brakes.show_info(self)
        Door.show_info(self)
        Vehicle_interior.show_info(self)


mockvich_408 = Car('Москвич', '408', 'Синий', 'Седан', 'Рычажная, рессоры',
                   'Задний', 'R13', 1.5, 4, 'Бензин 76',
                   'Механическая', 4, 'Барабанные',
                   'Классчическое, петельное', 'Кожзам')

lamborghini = Car('Lamborghini', 'Aventador', 'Красный', 'Купе', 'Независимая подвеска, амортизация',
                  'Полный', 'R20', 6.5, 12, 'Бензин 98',
                  'Автоматическая', 7, 'Керамические',
                  'Многорычажное, двойное', 'Натуральная кожа')

mockvich_408.show_info()
print()
lamborghini.show_info()

# Задание 1
class Fraction:
    count = 0

    def __init__(self, numer, denom):
        self.__numer = numer
        self.__denom = denom
        Fraction.count += 1

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
            print('Знаменатель не может быть нулем.')

    def add(self, fract):
        result_num = self.__numer * fract.denom + fract.numer * self.__denom
        result_denom = self.__denom * fract.denom
        return Fraction(result_num, result_denom)

    def subtract(self, fract):
        result_num = self.__numer * fract.denom - fract.numer * self.__denom
        result_denom = self.__denom * fract.denom
        return Fraction(result_num, result_denom)

    def multiply(self, fract):
        result_num = self.__numer * fract.numer
        result_denom = self.__denom * fract.denom
        return Fraction(result_num, result_denom)

    def divide(self, fract):
        if fract.numer != 0:
            result_num = self.__numer * fract.denom
            result_denom = self.__denom * fract.numer
            return Fraction(result_num, result_denom)
        else:
            print('Деление на нуль')

    def to_string(self):
        return f"{self.__numer}/{self.__denom}"

    @staticmethod
    def count_class_obj():
        return f'Количество созданных объектов: {Fraction.count}'


fract1 = Fraction(1, 2)
fract2 = Fraction(3, 4)
fract3 = Fraction(6, 4)

print('Дробь 1:', fract1.to_string())
print("Дробь 2:", fract2.to_string())

result_add = fract1.add(fract2)
print('Результат сложения:',
      result_add.to_string())  # результатом новый экземпляр класса

result_sub = fract1.subtract(fract2)  # результатом новый экземпляр класса
print('Результат вычитания:', result_sub.to_string())

result_multip = fract1.multiply(fract2)  # результатом новый экземпляр класса
print('Результат умножения:', result_multip.to_string())

result_div = fract1.divide(fract2)  # результатом новый экземпляр класса
print('Результат деления:', result_div.to_string())

print(Fraction.count_class_obj())  # и тогда здесь будет 7


# Задание 2
class TemperatureConverter:
    conversion_count = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConverter.conversion_count += 1
        return (celsius * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConverter.conversion_count += 1
        return (fahrenheit - 32) * 5 / 9

    @classmethod
    def get_conversion_count(cls):
        return cls.conversion_count


print(TemperatureConverter.celsius_to_fahrenheit(25))
print(TemperatureConverter.fahrenheit_to_celsius(77))
print(TemperatureConverter.get_conversion_count())


# Задание 3

class Device:
    def __init__(self, name, model, manufacturer, power):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.power = power

    def set_name(self, new_name):
        self.name = new_name

    def set_model(self, new_model):
        self.model = new_model

    def set_manufacturer(self, new_manufacturer):
        self.manufacturer = new_manufacturer

    def set_power(self, new_power):
        self.power = new_power

    def get_name(self):
        return self.name

    def get_model(self):
        return self.model

    def get_manufacturer(self):
        return self.manufacturer

    def get_power(self):
        return self.power

    def show_info(self):
        print('Информация:')
        print('Название:', self.name)
        print('Модель:', self.model)
        print('Производитель:', self.manufacturer)
        print('Мощность:', self.power)


class CoffeeMachine(Device):
    def __init__(self, name, model, manufacturer, power, coffee_type):
        super().__init__(name, model, manufacturer, power)
        self.coffee_type = coffee_type

    def set_coffee_type(self, new_coffee_type):
        self.coffee_type = new_coffee_type

    def get_coffee_type(self):
        return self.coffee_type

    def show_info(self):
        super().show_info()
        print('Тип кофе:', self.coffee_type)


class Blender(Device):
    def __init__(self, name, model, manufacturer, power, speed_levels):
        super().__init__(name, model, manufacturer, power)
        self.speed_levels = speed_levels

    def set_speed_levels(self, new_speed_levels):
        self.speed_levels = new_speed_levels

    def get_speed_levels(self):
        return self.speed_levels

    def show_info(self):
        super().show_info()
        print('Уровни скорости:', self.speed_levels)


class MeatGrinder(Device):
    def __init__(self, name, model, manufacturer, power, grinder_type):
        super().__init__(name, model, manufacturer, power)
        self.grinder_type = grinder_type

    def set_grinder_type(self, new_grinder_type):
        self.grinder_type = new_grinder_type

    def get_grinder_type(self):
        return self.grinder_type

    def show_info(self):
        super().show_info()
        print('Тип привода:', self.grinder_type)


device1 = Device('Device 1', 'Model 1', 'Manufacturer 1', 1000)
device1.show_info()

coffee_machine1 = CoffeeMachine('Coffee Machine 1', 'Model A', 'Brand X', 1200,
                                'Espresso')
coffee_machine1.show_info()

blender1 = Blender('Blender 1', 'Model C', 'Brand Z', 800, 5)
blender1.show_info()

meat_grinder1 = MeatGrinder('Meat Grinder 1', 'Model E', 'Brand V', 1200,
                            'Electric')
meat_grinder1.show_info()


# Задание 4

class Weapon:
    def __init__(self, type_gunpowder, barrel_type):
        self._type_gunpowder = type_gunpowder
        self._barrel_type = barrel_type

    @property
    def type_gunpowder(self):
        return self._type_gunpowder

    @type_gunpowder.setter
    def type_gunpowder(self, new_type_gunpowder):
        self._type_gunpowder = new_type_gunpowder

    @property
    def barrel_type(self):
        return self._barrel_type

    @barrel_type.setter
    def barrel_type(self, new_barrel_type):
        self._barrel_type = new_barrel_type

    def show_info(self):
        print(f'Тип пороха: {self._type_gunpowder}')
        print(f'Тип ствола: {self._barrel_type}')


class Revolver(Weapon):
    def __init__(self, type_gunpowder, barrel_type, number_cartridges):
        super().__init__(type_gunpowder, barrel_type)
        self._number_cartridges = number_cartridges

    @property
    def number_cartridges(self):
        return self._number_cartridges

    @number_cartridges.setter
    def number_cartridges(self, new_number_cartridges):
        self._number_cartridges = new_number_cartridges

    def show_info(self):
        super().show_info()
        print(f'Количество патронов в барабане: {self._number_cartridges}')


class Revolving_rifle(Revolver):
    def __init__(self, type_gunpowder, barrel_type, number_cartridges,
                 barrel_len):
        super().__init__(type_gunpowder, barrel_type, number_cartridges)
        self._barrel_length = barrel_len

    @property
    def barrel_length(self):
        return self._barrel_length

    @barrel_length.setter
    def barrel_length(self, new_barrel_length):
        self._number_cartridges = new_barrel_length

    def show_info(self):
        super().show_info()
        print(f'Длина ствола: {self._barrel_length} m.')


class Shooting_turret(Device, Revolving_rifle):
    def __init__(self, name, model, manufacturer, power, type_gunpowder,
                 barrel_type, number_cartridges, barrel_len):
        Device.__init__(self, name, model, manufacturer, power)
        Revolving_rifle.__init__(self, type_gunpowder, barrel_type,
                                 number_cartridges, barrel_len)

    def show_info(self):
        Device.show_info(self)
        Revolver.show_info(self)


primitiv_weapon = Weapon('Чёрный порох', 'Гладкоствольный')
primitiv_weapon.show_info()
revolver1 = Revolver('Бездынмый порох', 'Нарезной', 6)
revolver1.show_info()
revolver_rifle = Revolving_rifle('Бездымный', 'Нарезной', 8, 0.84)
revolver_rifle.show_info()
print()
print('Тестовая турель')
print()
portal2 = Shooting_turret('Турель J2FE', 'K2567',
                          'Портал 2', 2000,
                          'Бездымный',
                          'Нарезной', 8, 1.24)
portal2.show_info()

'''Скучно было переписывать с дейвайсов на корабли)'''

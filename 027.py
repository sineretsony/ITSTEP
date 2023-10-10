# class Car:
#     def __init__(self, color, name, speed):
#         print('init working')
#         self.__color = color
#         self.name = name
#         self.__speed = speed
# #
#     def __del__(self):
#         print('Car removed')
#
#     def show_info(self):
#         print(f'Name: {self.name}, '
#               f'Color: {self.__color}, '
#               f'Speed: {self.__speed} km/h')
#
#     def set_color(self, new_color):
#         self.__color = new_color
#
#     def set_name(self, new_name):
#         self.name = new_name
#
#     def get_color(self):
#         return self.__color
#
#     def get_name(self):
#         return self.name
#
#     @property
#     def speed(self):
#         return self.__speed
#
#     @speed.setter
#     def speed(self, new_speed):
#         self.__speed = new_speed
#
#
# myCar = Car('white', 'Ferrari', 200)
# myCar2 = Car('blue', 'Ferrari', 200)
# myCar.show_info()
# myCar2.show_info()
# myCar.show_info()
# myCar.show_info()


class Student:
    def __init__(self, first_last_name, date, phone, city):
        self.__first_last_name = first_last_name
        self.__date_birth = date
        self.__phone_number = phone
        self.__city = city

    def input_data(self, first_last_name, date_of_birth, phone_number, city):
        self.__first_last_name = first_last_name
        self.__date_birth = date_of_birth
        self.__phone_number = phone_number
        self.__city = city

    def display_data(self):
        print('Student Information:')
        print(f'Full Name: {self.__first_last_name}')
        print(f'Date of Birth: {self.__date_birth}')
        print(f'Phone Number: {self.__phone_number}')
        print(f'City: {self.__city}')

    def get_full_name(self):
        return self.__first_last_name

    def get_date_of_birth(self):
        return self.__date_birth

    def get_phone_number(self):
        return self.__phone_number

    def get_city(self):
        return self.__city

    def set_full_name(self, new_name):
        self.__first_last_name = new_name

    def set_date_of_birth(self, new_date):
        self.__date_birth = new_date

    def set_phone_number(self, new_phone):
        self.__phone_number = new_phone

    def set_city(self, new_city):
        self.__city = new_city


st1 = Student('Иван Иванов', '22.01.2000', '096333333', 'Odessa')
st1.display_data()

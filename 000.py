class Test:
    # переменная класса (атрибут класса)
    count = 0

    # конструктор класса
    def __init__(self, test_01, test_02):
        # атрибуты объекта
        self.test_01 = test_01
        # защищёное поле объекта доступно дочерним классам
        self._test_02 = test_02
        # приватное поле объекта не доступно дочерним классам
        self.__private_var = 42

    # метод объекта для установки значения атрибута test_01 (свойство объекта)
    def set_test_01(self, new_test_01):
        self.test_01 = new_test_01

    # метод объекта для получения значения атрибута test_01 (свойство объекта)
    def get_test_01(self):
        return self.test_01

    # свойство класса для доступа к атрибуту _test_02
    @property
    def test_pr(self):
        return self._test_02

    # setter для свойства test_pr
    @test_pr.setter
    def test_pr(self, new_test_02):
        self._test_02 = new_test_02

    # статический метод класса
    @staticmethod
    def static_method():
        print("Это статический метод")

    # деструктор
    def __del__(self):
        print("Объект уничтожен")


test_object = Test(1, 2)
# Вызов статического метода
Test.static_method()

'''Gregoire Gorea, [13.10.2023 16:59]----------
класс - это шаблон, который определяет структуру и поведение объекта. 
Объект - это экземпляр класса.

Gregoire Gorea, [14.10.2023 13:07]-------------
Свойства - это специальные методы, которые предоставляют доступ к полям класса.

Gregoire Gorea, [14.10.2023 13:07]-------------
@property - это декоратор в Python, который позволяет нам создавать свойства для классов

Gregoire Gorea, [14.10.2023 13:20]--------------
Атрибут - это переменная, которая принадлежит объекту. Атрибуты могут быть как публичными, так и закрытыми.

Gregoire Gorea, [14.10.2023 13:21]--------------
Метод класса - это метод, который принадлежит классу, а не объекту. 
Методы класса обычно используются для выполнения операций, которые не зависят от конкретного объекта.
------------------------------------------------
Метод str может быть использован для преобразования объектов в строку 
для вывода в консоль, для хранения в файле или для передачи в другие функции.

---------------------------
Статический метод в Python классах - это метод, который привязан к классу, 
а не к экземпляру этого класса. Он не имеет доступа к атрибутам и методам
 экземпляра класса и не может изменять их состояние. 
 Статический метод определяется с использованием декоратора @staticmethod.'''
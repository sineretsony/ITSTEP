import json


class TestClass:
    pass


#
# obj = TestClass()
#
# print(type(type(obj)))

def method1(self):
    print('hello')


NewClass = type('NewClass', (TestClass,), {'attr0': 123, 'method': method1})


# obj1 = NewClass()
# print(obj1)
# print(type(obj1))
# print(obj1.attr0)
# obj1.method()


# class MyMetaClass(type):
#     def __new__(cls, name, bases, dict):
#         print('Type class created', cls)
#         print('name class', name)
#         print('basses list', bases)
#         print('list attr', dict)
#         return type.__new__(cls, name, bases, dict)
#
#
# class MyClass1(metaclass=MyMetaClass):
#     attr = 1
#
#
# print(type(MyMetaClass))
# print(type(MyClass1))

#
# class MyMetaClass(type):
#     def __new__(cls, name, bases, dict):
#         if 'id' not in dict.keys():
#             print('not id attr in class')
#         else:
#             methods = {key: v for key, v in dict.items() if callable(v)}
#             if len(methods) > 2:
#                 print('More than 2 methods!')
#             else:
#                 print('class is criated', name)
#                 return type.__new__(cls, name, bases, dict)
#
#
# class MyMetaClass2(type):
#     def __new__(cls, name, bases, dict):
#         resultClass = super().__new__(cls, name, bases, dict)
#         if 'id' not in dict.keys():
#             print('not id attr in class')
#             resultClass.id = 0
#         return resultClass
#
#
# class MyClass1(metaclass=MyMetaClass):
#     attr = 1
#
#
# class MyClass2(metaclass=MyMetaClass):
#     attr = 1
#     id = 0
#
#     def method1(self):
#         pass
#
#     def method2(self):
#         pass
#
#     def method3(self):
#         pass
#
#
# class User(metaclass=MyMetaClass2):
#     attr = 3
#
#
# class MyMetaClass3(type):
#     def __new__(cls, name, bases, dict, **kwargs):
#         resultClass = super().__new__(cls, name, bases, dict)
#         if kwargs:
#             for k, v in kwargs.items():
#                 setattr(resultClass, k, v)
#         return resultClass
#
#
# class User2(metaclass=MyMetaClass3, firtsname='Joe', age=30):
#     attr = 3
#
#
# user = User2()
# print(user.firtsname)

# class MyMeta(type):
#     def __init__(cls, name, bases, dict):
#         for k, v in dict.items():
#             if not k.islower():
#                 raise ValueError('attr must be lowercase!')
#
#         super().__init__(name, bases, dict)
#
#
# class MyClass(metaclass=MyMeta):
#     Name = 'test'
# import json
#
#
# class JSONSerializableMeta(type):
#     def __new__(cls, name, bases, dict):
#         dict['to_json'] = lambda self: json.dumps(self.__dict__)
#         dict['from_json'] = classmethod(lambda cls, json_str: cls(**json.loads(json_str)))
#         return super().__new__(cls, name, bases, dict)
#
#
# class Person(metaclass=JSONSerializableMeta):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# person = Person('Alise', 40)
# json_data = person.to_json()
# print(json_data)
#
# new_person = Person.from_json(json_data)
#
# print(new_person.name)

# # Задание 1
# class Registry_class_meta(type):
#     registry = {}
#
#     def __new__(cls, name, bases, dct):
#         temp = super().__new__(cls, name, bases, dct)
#         cls.registry[name] = temp
#         return temp
#
#
# class MyClass1(metaclass=Registry_class_meta):
#     pass
#
#
# class MyClass2(metaclass=Registry_class_meta):
#     pass
#
#
# print(Registry_class_meta.registry)
#
#
# # Задание 2
# class Check_str_attr_meta(type):
#     def __new__(cls, name, bases, dct):
#         for name, value in dct.items():
#             if not isinstance(value, str):
#                 raise AttributeError(f'attribute \"{name}\" type must be str!')
#         return super().__new__(cls, name, bases, dct)
#
#
# class MyClass3(metaclass=Check_str_attr_meta):
#     attr = ''
#
#
# # class MyClass4(metaclass=Check_str_attr_meta):
# #     attr = 0

# Задание 3
# class ContainerMeta(type):
#     def __new__(cls, name, bases, dct):
#         dct['container'] = []
#
#         dct['add_item'] = lambda self, item: self.container.append(item)
#         dct['remove_item'] = lambda self, item: self.container.remove(item) if item in self.container else None
#         dct['find_item'] = lambda self, item: item in self.container
#         dct['__str__'] = lambda self: f'{self.container}'
#
#         return super().__new__(cls, name, bases, dct)
#
#
# class MyContainerClass(metaclass=ContainerMeta):
#     def __init__(self, name):
#         self.name = name
#
#
# obj1 = MyContainerClass("Object 1")
# obj2 = MyContainerClass("Object 2")
#
# obj1.add_item(obj1)
# obj1.add_item(obj2)
#
# print(obj1.container)
# print(obj1.find_item(obj1))
# print(obj1.find_item(obj2))
#
# obj1.remove_item(obj1)
# print(obj1.container)
# Получаем код от пользователя

def test():
    print(2323323233)


code_to_execute = input("Введите код для выполнения: ")
try:
    exec(code_to_execute)
except Exception as e:
    print(f"Произошла ошибка: {e}")

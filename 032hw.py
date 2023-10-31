# Задание 1
class AttributeMonitor(type):
    def __new__(cls, name, bases, attrs):
        print(f"Создание класса: {name}")
        print(f"Атрибуты класса: {attrs}")
        return super().__new__(cls, name, bases, attrs)


class MonitoredClass(metaclass=AttributeMonitor):
    def __init__(self, value):
        self.value = value

    def show_info(self):
        print(f"Значение атрибута: {self.value}")


obj = MonitoredClass(2)
obj.show_info()


# Задание 2
class CodeGenerationMeta(type):
    def __new__(cls, name, bases, attrs):
        new_attrs = cls.generate_methods(attrs)
        return super().__new__(cls, name, bases, new_attrs)

    @staticmethod
    def generate_methods(attrs):
        new_attrs = dict(attrs)
        for attr_name, attr_value in attrs.items():
            if attr_name.endswith("_") and not callable(attr_value):
                operation = attr_name.rstrip("_")
                method_name = f"perform_{operation}"
                new_attrs[method_name] = CodeGenerationMeta.generate_method(
                    operation)
        return new_attrs

    @staticmethod
    def generate_method(operation):
        def method(self, *args):
            if operation == "add":
                result = sum(args)
            elif operation == "subtract":
                result = args[0] - args[1]
            elif operation == "multiply":
                result = args[0] * args[1]
            else:
                result = None
            return result

        return method


class Calculator(metaclass=CodeGenerationMeta):
    add_ = None
    subtract_ = None
    multiply_ = None

    def __init__(self):
        pass


calc = Calculator()

print(calc.perform_add(1, 2, 3))
print(calc.perform_subtract(5, 2))
print(calc.perform_multiply(4, 3))

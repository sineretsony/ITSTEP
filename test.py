# a = 'fff50002000hhhh545'
#
#
# def extract(string):
#     result = ''
#     temp = ''
#     if isinstance(string, str):
#         for i in string:
#             if i.isdigit():
#                 temp += str(i)
#             elif i.isalpha() and len(temp) != 0:
#                 if len(temp) != 0:
#                     result, temp = temp, ''
#         if len(temp) != 0 and len(result) == 0:
#             result, temp = temp, ''
#         if len(result) > 0 and len(temp) > 0:
#             raise TypeError("Unsupported operand type")
#         if len(result) != 0:
#             return int(result)
#     return 0
#
#
# print(extract(a))
#
# class Test:
#     def __init__(self, a, b):
#         if isinstance(a, str):
#             self.a = self.__extract(a)
#         else:
#             self.a = a
#         if isinstance(b, str):
#             self.b = self.__extract(b)
#         else:
#             self.b = b
#
#     @classmethod
#     def __extract(cls, string):
#         result = ''
#         temp = ''
#         if isinstance(string, str):
#             for i in string:
#                 if i.isdigit():
#                     temp += str(i)
#                 elif i.isalpha() and len(temp) != 0:
#                     if len(temp) != 0:
#                         result, temp = temp, ''
#             if len(temp) != 0 and len(result) == 0:
#                 result, temp = temp, ''
#             if len(result) > 0 and len(temp) > 0:
#                 raise TypeError("Unsupported operand type")
#             if len(result) != 0:
#                 return int(result)
#         return 0
#
#     def show_info(self):
#         print(type(self.a))
#         print(self.a)
#         print(type(self.b))
#         print(self.b)
#
#
# c = Test('aaa10', 'hgh20jk')
# c.show_info()

def adder(*args, **kwargs):
    result = 0
    for value in args:
        if type(value) == int or type(value) == float or type(value) == bool:
            result += value
        elif type(value) == list or type(tuple):
            for i in value:
                result += i
        else:
            try:
                result += float(value)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(value)
                continue
            except (ValueError, TypeError):
                pass

    for value in kwargs.values():
        if type(value) == int or type(value) == float or type(value) == bool:
            result += value
        else:
            try:
                result += float(value)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(value)
                continue
            except (ValueError, TypeError):
                pass

    return result

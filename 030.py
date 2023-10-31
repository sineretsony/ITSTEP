# class Droid:
#     def __init__(self):
#         pass
#
#     def print_class_name(self):
#         print("Droid")
# class C3PO(Droid):
#     def __init__(self):
#         super().__init__()
#     def print_class_name(self):
#         super().print_class_name()
#         print("C3PO")
# class R2D2(Droid):
#     def __init__(self):
#         super().__init__()
#     def print_class_name(self):
#         super().print_class_name()
#         print("R2D2")
# class BBB(R2D2):
#     def __init__(self):
#         super().__init__()
#     def print_class_name(self):
#         super().print_class_name()
#         print("BBB")
#
# droid = Droid()
# c3po = C3PO()
# r2d2 = R2D2()
# bbb = BBB()
#
# droid.print_class_name()
# c3po.print_class_name()
# r2d2.print_class_name()
# bbb.print_class_name()

# class Film:
#     def __new__(cls, *args, **kwargs):
#         print('new film created')
#         return super(Film, cls).__new__(cls)
#
#     def __init__(self, title, genre):
#         print(f'init film working')
#         self.title = title
#         self.genre = genre
#
#     def show_info(self):
#         print(f'Title: {self.title}')
#         print(f'Genre: {self.genre}')
#
#
# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages
#
#     def show_info(self):
#         print(f'Title: {self.title}')
#         print(f'Page: {self.pages}')
#
#     def __str__(self):
#         return f'Title: {self.title}\nPage: {self.pages}'
#
#     def __eq__(self, other):
#         return self.title == other.title and self.pages == other.pages
#
#     def __gt__(self, other):
#         return self.pages > other.pages
#
#     def __lt__(self, other):
#         return self.pages < other.pages
#
#     def __ne__(self, other):
#         return self.pages != other.pages
#
#
# # film1 = Film('Matrix', 'fantastic')
# book1 = Book('Python course', 300)
# book2 = Book('Python course', 600)
#
# # for item in (film1, book1):
# #     item.show_info()
#
# # print(book1 + book2)
# # print(book1 == book2)
# print(book1 < book2)


# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.feedback = [2, 4, 5, 6, 7]
#
#     def __str__(self):
#         return f'x: {self.x} y: {self.y}\n'
#
#     def __float__(self):
#         return Vector(float(self.x), float(self.y))
#
#     def __add__(self, otherV):
#         if isinstance(otherV, Vector):
#             return Vector(self.x + otherV.x, self.y + otherV.y)
#         elif isinstance(otherV, int):
#             return Vector(self.x + otherV, self.y + otherV)
#
#     def __iadd__(self, other):
#         if isinstance(other, Vector):
#             self.x += other.x
#             self.y += other.y
#             return self
#         elif isinstance(other, int):
#             self.x += other
#             self.y += other
#             return self
#
#     def __getitem__(self, ind):
#         if 0 <= ind <= max(self.feedback):
#             return self.feedback[ind]
#         else:
#             return -1
#
#
# vector1 = Vector(1, 1)
# vector2 = Vector(2, 2)
# vector1 += vector2
# print(vector1.__float__())
#
# print(vector1 + vector2)
# print(vector1 + 3)
#
# print(vector1[2])
# Задание 1
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        elif isinstance(other, int):
            return self.radius == other

    def __ne__(self, other):
        if isinstance(other, Circle):
            return self.radius != other.radius
        elif isinstance(other, int):
            return self.radius != other

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        elif isinstance(other, int):
            return self.radius < other

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        elif isinstance(other, int):
            return self.radius > other

    def __iadd__(self, other):
        if isinstance(other, int):
            self.radius += other
            return self
        else:
            raise TypeError("Unsupported operand type")

    def __isub__(self, other):
        if isinstance(other, int):
            self.radius -= other
            return self
        else:
            raise TypeError("Unsupported operand type")

    def __add__(self, other):
        if isinstance(other, int):
            return Circle(self.radius + other)
        else:
            raise TypeError("Unsupported operand type")

    def __sub__(self, other):
        if isinstance(other, int):
            return Circle(self.radius - other)
        else:
            raise TypeError("Unsupported operand type")

    def __str__(self):
        return f"{self.radius}"


circle1 = Circle(50)
circle2 = Circle(30)

print(circle1 == circle2)
print(circle1 > circle2)

circle1 += 10
print(circle1.radius)

circle1 -= 5
print(circle1.radius)


# Задание 2
class Airplane:
    def __init__(self, type, max_pas):
        self.type = type
        self.max_pas = max_pas

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.type == other.type
        return False

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.max_pas > other.max_pas
        return False

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.max_pas < other.max_pas
        return False


plane1 = Airplane("Boeing 747", 420)
plane2 = Airplane("Airbus A380", 850)
plane3 = Airplane("Boeing 737", 230)

print(plane1 == plane3)
print(plane2 > plane1)

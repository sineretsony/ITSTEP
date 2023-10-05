# Задание 1
print("\nЗадание 1\n")

input_data = [('Интерстеллар', 2014, 'Кристофер Нолан'),
              ('Матрица', 1999, 'Лана Вачовски'),
              ('История игрушек', 1995, 'Джон Лассетер'),
              ('Гравитация', 2013, 'Альфонсо Куарон')]


def movFilter(d, year):
    temp = []
    for movie in d:
        if movie[1] >= year:
            temp.append(", ".join(str(item) for item in movie))
    return "\n".join(temp)


print(movFilter(input_data, 2000))

# Задание 2
print("\nЗадание 2\n")

input_data2 = [('Иванов', 'Группа 1', 4.5),
               ('Петров', 'Группа 2', 3.8),
               ('Сидорова', 'Группа 1', 4.2),
               ('Смирнов', 'Группа 2', 4.1)]


def maximum_minimum(d):
    max_g = max(d, key=lambda x: x[2])[2]
    min_g = min(d, key=lambda x: x[2])[2]

    temp_max = []
    temp_min = []

    for s in d:
        if s[2] == max_g:
            temp_max.append(", ".join(str(i) for i in s))
        elif s[2] == min_g:
            temp_min.append(", ".join(str(i) for i in s))

    return "\n".join(temp_max) + "\n" + "\n".join(temp_min)


print(maximum_minimum(input_data2))

# Задание 3
print("\nЗадание 3\n")

input_data3 = [('Барселона', 120, 20),
               ('Реал Мадрид', 110, 30),
               ('Манчестер Юнайтед', 90, 40),
               ('Бавария', 100, 20)]


def soccerFilter(d, vi):
    temp = []
    for m in d:
        if m[1] >= vi:
            temp.append(": ".join([str(m[0]), str(m[1])]))
    return "\n".join(temp)


print(soccerFilter(input_data3, 100))

# Задание 4
print("\nЗадание 4\n")

input_data4 = [('Мастер и Маргарита', 'Михаил Булаков', 1967),
               ('Преступление и наказание', 'Федор Достоевский', 1866),
               ('Война и мир', 'Лев Толстой', 1869),
               ('1984', 'Джордж Оруэлл', 1949)]


def author(a):
    temp = set(map(lambda x: x[1], a))
    result = "\n".join(temp)
    return result


print(author(input_data4))

# Задание 5 доп
print("\nЗадание 5\n")

wood = [(i, j) for i in range(8) for j in range(8)]


def blackWhite(coord):
    coord_sum = coord[0] + coord[1]
    if coord_sum % 2 == 0:
        return "White"
    else:
        return "Black"


def woodPrint(x):
    global king
    global queen
    result = []
    temp = []

    for i in x:
        cv = blackWhite(i)
        if i == king:
            temp.append("♔")
        elif i == queen:
            temp.append("♕")
        elif cv == "White":
            temp.append("🌕")
        elif cv == "Black":
            temp.append("🌑")

        if len(temp) == 8:
            temp.append("\n")
            result.extend(temp)
            temp = []
    return ''.join(result)


king = (4, 0)
queen = (3, 7)


def motion_check(figure, coord, new_coord, status=False):
    x, y = coord

    if figure == "king":
        rules = [(x + dx, y + dy)
                 for dx in [-1, 0, 1]
                 for dy in [-1, 0, 1]
                 if (dx != 0 or dy != 0)]

    elif figure == "queen":
        vertical_moves = [(x, i) for i in range(8) if i != y]
        horizontal_moves = [(i, y) for i in range(8) if i != x]
        diagonal_moves = [(x + i, y + i)
                          for i in range(-min(x, y), min(8 - x, 8 - y))
                          if i != 0] + \
                         [(x + i, y - i)
                          for i in range(-min(x, 7 - y), min(8 - x, y + 1))
                          if i != 0]

        rules = vertical_moves + horizontal_moves + diagonal_moves
    else:
        return None

    valid_moves = [(dx, dy) for dx, dy in rules if
                   0 <= dx <= 7 and 0 <= dy <= 7]

    if status:
        return valid_moves
    else:
        return tuple(new_coord) in valid_moves


print("Проверка на доступность хода", "king",
      motion_check("king", king, (4, 2)))
print("Проверка на доступность хода", "queen",
      motion_check("queen", queen, (3, 1)))
print("Цвет клетки (0, 0):", blackWhite((0, 0)))
print("Цвет клетки (1, 0):", blackWhite((1, 0)))
print(woodPrint(wood))

while True:
    action = input("Выберете фигуру: 1 - король, 2 - ферзь, 3 - выход: ")

    if action == "1":
        new_king_coordinates = tuple(
            map(int, input("Введите новые координаты короля (x y): ").split()))
        if motion_check("king", king, new_king_coordinates):
            king = new_king_coordinates
        else:
            print("Недопустимое перемещение для короля.")

    elif action == "2":
        new_queen_coordinates = tuple(
            map(int, input("Введите новые координаты ферзя (x y): ").split()))
        if motion_check("queen", queen, new_queen_coordinates):
            queen = new_queen_coordinates
        else:
            print("Недопустимое перемещение для ферзя.")

    elif action == "3":
        break

    print(woodPrint(wood))

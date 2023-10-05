from random import randint


# Задание 1
def speed_distance(s, d):
    time = d / s
    result = time * 60
    return int(result)


def speed_time(s, t):
    result = s * t
    return result


speed = 130
distance = 100
time_hours = 1.0

time_minutes = speed_distance(speed, distance)
distance_traveled = speed_time(speed, time_hours)

print(f"Скорость: {speed} км/ч")
print(f"Расстояние: {distance} км")
print(f"Время в пути: {time_minutes} минут")
print(f"Проеханное расстояние: {distance_traveled} км")


# Задание 2
def truth_lie(n):
    if n > 0:
        return True
    elif n < 0:
        return False
    else:
        return None


print(truth_lie(5))
print(truth_lie(-5))
print(truth_lie(0))


# Задание 3
def start_end_num(n):
    temp_list = [str(i) for i in range(1, n + 1)]
    return ", ".join(temp_list)


print(start_end_num(6))

# Задание 4

num = [1, 56, 45, 7, 67, 34, 56]


def mim_and_max(m):
    max_num = max(m)
    min_num = min(m)
    index_max = m.index(max_num)
    index_min = m.index(min_num)
    return max_num, index_max, min_num, index_min


max_num1, index_max1, min_num1, index_min1 = mim_and_max(num)

print(f"Максимальное значение {max_num1}, индекс в списке {index_max1}\n"
      f"Минимальное значение {min_num1}, индекс в списке {index_min1}")

# Задание 5

num2 = [1, 56, 45, 7, 67, 34, 56]


def average(s):
    summ_list = sum(s)
    aver = summ_list / len(s)
    return aver


print(f"Среднее арифметическое списка {average(num2)}")

# Задание 6

num3 = [1, 56, 45, 7, 67, 34, 56]


def revers_list(n):
    result = n[::-1]
    return result


print(revers_list(num3))


# Задание 7

def start_end_sum(s, e):
    results = sum([i for i in range(s, e + 1)])
    return results


print(start_end_sum(4, 50))

# Задание 8

num4 = [1, -56, 45, -7, 67, 34, 56, 0, 2, -67, 0]


def number_counter(s):
    pos = 0
    neg = 0
    zero = 0

    for i in s:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1

    return pos, neg, zero


pos_count, neg_count, zero_count = number_counter(num4)

print("Количество положительных чисел:", pos_count)
print("Количество отрицательных чисел:", neg_count)
print("Количество нулей:", zero_count)


# Задание 9

def is_lucky_number(number):
    number_str = str(number)

    if len(number_str) != 6:
        return False

    left_sum = 0
    right_sum = 0

    for index, digit in enumerate(number_str):
        if index < 3:
            left_sum += int(digit)
        else:
            right_sum += int(digit)

    return left_sum == right_sum


print(is_lucky_number(554554))


# Задание 10

def generate_random_numbers(numbers, start, end, paired=False):
    nums = []
    for i in range(numbers):
        num = randint(start, end)
        if paired and num % 2 != 0:
            num += 1
        nums.append(num)
    return nums


print(generate_random_numbers(5, 10, 100))
print(generate_random_numbers(5, 10, 100, True))

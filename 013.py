# hours = float(input("Отработанные часы: "))
# zp = float(input("Введите ставку: "))
# clc = hours * zp
#
# print(f"Сумма заработной платы: {clc}")

# number = 39
# if number > 38:
#     print("sold")
#
# chack = True
#
# if chack:
#     print("chack = ", chack)
# else:
#     print("Ok")

# month_num = int(input("enter num month - "))
# if month_num == 1:
#     print(1)
# elif month_num == 2:
#     print(2)
# elif month_num == 3:
#     print(3)
# elif month_num == 4:
#     print(4)
# elif month_num == 5:
#     print(5)
# elif month_num == 6:
#     print(6)

# num = 100
# if 0 < num < 1000:
#     print("> 0 < 1000")
#
# if num >= 100 or num < 30:
#     print("num > 0 and < 100")

# user_num = int(input("Enter num "))
#
# if user_num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# user_num2 = int(input("Enter num "))
# if user_num2 % 7 == 0:
#     print("multiple of 7")
# else:
#     print("not a multiple of 7")

# user_num3 = 5
# user_num4 = 2
# if user_num3 < user_num4:
#     print("min", user_num3)
# elif user_num3 > user_num4:
#     print("min", user_num4)
# else:
#     print("equel")
#
# user_num5 = int(input("Enter num 1 "))
# user_num6 = int(input("Enter num 2 "))
# if user_num5 > user_num6:
#     print("max", user_num5)
# elif user_num5 < user_num6:
#     print("max", user_num6)
# else:
#     print("equel")

# num1 = int(input("Enter num 1: "))
# num2 = int(input("Enter num 2: "))
# oper = input("Enter +, -, average(3), *: ")
#
# if oper == "+":
#     print(num1 + num2)
# elif oper == "-":
#     print(num1 - num2)
# elif oper == "average" or oper == "3":
#     print((num1 + num2) / 3)
# elif oper == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator")


# ps4_cost = float(input("Enter game console cost "))
# number_of_consoles = int(input("Number of game consoles "))
# discount_percentage = float(input("Enter discount percentage:"))
#
# discount_amount = discount_percentage / 100
# total_cost = ps4_cost * number_of_consoles
# console_price = ps4_cost * (1 - discount_amount)
# choice = input("What do you want to count? total order value (1)"
#                "or the cost of one game console, taking into account "
#                "the discount (2):")
#
# if choice == "1":
#     print("The total cost of the order is:", total_cost)
# elif choice == "2":
#     print("The cost of one game console, taking into account the discount, is:"
#           , console_price)
# else:
#     print("Wrong choice.")
#
#
# meters = float(input("Enter the number of meters:"))
# unit = input("What unit of measure do you want to convert to? miles"
#              "(1), inches (2) or yards (3):")
#
# if unit == "1":
#     miles = meters / 1609.344
#     print("The number of miles is:", miles)
# elif unit == "2":
#     inches = meters * 39.37
#     print("The number of inches is:", inches)
# elif unit == "3":
#     yards = meters / 0.9144
#     print("The number of yards is:", yards)
# else:
#     print("Wrong choice.")


# number = int(input("Enter a number from 1 to 100:"))
#
# if 1 <= number <= 100:
#     result = ""
#     if number % 3 == 0:
#         result += "Fizz"
#     if number % 5 == 0:
#         result += "Buzz"
#     if not result:
#         result = number
#     print(result)
# else:
#     print("Error: number must be between 1 and 100")

# dist_AB = float(input("Enter the distance between points A and B (in km): "))
# dist_BC = float(input("Enter the distance between points B and C (in km): "))
# weight = float(input("Enter the weight of the cargo (in kg): "))
#
# fuel = None
# if weight <= 500:
#     fuel = weight * 1
# elif weight <= 1000:
#     fuel = weight * 4
# elif weight <= 1500:
#     fuel = weight * 7
# elif weight <= 2000:
#     fuel = weight * 9
#
# if fuel is None:
#     print("The plane can't lift that much weight.")
# else:
#     total_dist = dist_AB + dist_BC
#
#     if fuel > 300:
#         print("The fuel requirement exceeds the capacity of the fuel tank.")
#     else:
#         max_f = 300 / fuel
#
#         if max_f >= total_dist:
#             print("Refueling is not required.")
#         else:
#             req_fuel = (total_dist - max_f) * fuel
#
#             if req_fuel > 600:
#                 print("The plane will not fly due to "
#                       "excessive fuel consumption.")
#             else:
#                 print(f"Need to refuel {req_fuel:.2f} liters of fuel.")










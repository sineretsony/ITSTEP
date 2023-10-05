# декораторы

def simpleDecorator(myFunction):
    print("Hello ! decorator working !")

    def simpleWrapper():
        print("Func start working !")
        myFunction()
        print("func end")

    return simpleWrapper


def simpleDecorator_v2(myFunction):
    print("Hello ! decorator working2 !")

    def simpleWrapper():
        print("Func start working2 !")
        myFunction()
        print("func end2")

    return simpleWrapper


@simpleDecorator
@simpleDecorator_v2
def sayHi():
    print("Welcome!")


sayHi()


# sayHi = simpleDecorator(simpleDecorator_v2(sayHi))

@simpleDecorator
def sayBuy():
    print("Buy!")


def simpleDecorator_v3(myFunction):
    print("Hello ! decorator working3 !")

    def simpleWrapper():
        print("Func start working3 !")
        result = myFunction()
        print("func end3")
        return result

    return simpleWrapper


def calcSum():
    x = 10
    y = 20
    return x + y


calcSum = simpleDecorator_v3(calcSum)
print(calcSum())


def simpleDecorator_v4(myFunction):
    print("Hello! Decorator working4!")

    def simpleWrapper(*args, **kwargs):
        print("Func start working4!")
        print(args, kwargs)
        result2 = myFunction(*args, **kwargs)
        print("func end4")
        return result2

    return simpleWrapper


@simpleDecorator_v4
def calcSum_v2(a, b, c):
    return a + b + c


result = calcSum_v2(2, 3, 5)
print("Result:", result)


def decoratorWrapper(argForDecorator):
    print(argForDecorator)

    def simpleDecorator_v5(myFunction):
        print("Hello! Decorator working5!")

        def simpleWrapper(*args, **kwargs):
            print("Func start working5!")
            print(args, kwargs)
            print("Argument for decorator:", argForDecorator)
            result2 = myFunction(*args, **kwargs)
            print("func end5")
            return result2

        return simpleWrapper

    return simpleDecorator_v5


@decoratorWrapper("")
def calcSum_v2(a, b, c):
    return a + b + c


result = calcSum_v2(2, 3, 5)
print("Result:", result)

######################################################################

#
# def setDiscountDecoratorWrapper(disc):
#     def changePriceDecorator_v1(myFunction):
#         print("start decorator")
#
#         def simpleWrapper(argList):
#             print("Input", argList)
#             result = myFunction(argList)
#             resultWithDisc = list(map(lambda x: x * (1 - disc), result))
#             return resultWithDisc
#
#         return simpleWrapper
#
#     return changePriceDecorator_v1
#
#
# priceUSD = [100, 35, 67, 45.5]
# print(priceUSD)
#
#
# @setDiscountDecoratorWrapper(0.50)
# def toPriceNew(priseList):
#     return list(map(lambda x: x * 38, priseList))
#
#
# print(toPriceNew(priceUSD))
#
# #######################################################################
#
# import time, random
#
#
# def checkTime(myFunction):
#     def wrapper(*args, **kwargs):
#         startTime = time.time()
#         result = myFunction(*args, **kwargs)
#         print(f"Working time {time.time() - startTime}")
#         return result
#
#     return wrapper
#
#
# @checkTime
# def testFunc():
#     print("func working")
#     time.sleep(1)
#
#
# testFunc()


import time

#
# # Задание 1
# def multiplierFuncDecorator(mult):
#     def simplDecorator(func):
#         def wrapper(*args, **kwargs):
#             tot_time = 0
#             for h in range(mult):
#                 start_time = time.time()
#                 result3 = func(*args, **kwargs)
#                 tot_time += time.time() - start_time
#             print(f"Average working time: {tot_time / mult:.6f} seconds")
#             return result3
#
#         return wrapper
#
#     return simplDecorator
#
#
# @multiplierFuncDecorator(3)
# def function():
#     time.sleep(1)
#     return "Final!"
#
#
# result = function()
# print(result)

# Задание 2


def retry_func(retry):
    def decorator(func):
        def wrapper(*args, **kwargs):
            temp_c = 0
            while temp_c < retry:
                try:
                    result5 = func(*args, **kwargs)
                    return result5
                except Exception:
                    temp_c += 1
            print("retry", retry)

        return wrapper

    return decorator


@retry_func(3)
def testFunc():
    if 1 % 2 == 0:
        # if 2 % 2 == 0:
        raise ValueError("Failed!")
    else:
        return "Final"


result = testFunc()
print(result)


# Задание 3
def func_counter(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Function calling : {count}")
        return func(*args, **kwargs)

    return wrapper


@func_counter
def testCountF(x):
    print(x)


testCountF("Hello1")
testCountF("Hello2")
testCountF("Hello3")
testCountF("Hello4")
testCountF("Hello5")
testCountF("Hello6")

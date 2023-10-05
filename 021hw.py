# Задание 1
def limiterDecorator(limit):
    def decorator(func):
        count = limit

        def wrapper(*args, **kwargs):
            nonlocal count
            if count > 0:
                count -= 1
                result = func(*args, **kwargs)
                return result
            else:
                print("Limit exceeded")
                return None

        return wrapper

    return decorator


@limiterDecorator(2)
def testPrint(t):
    print(t)


testPrint("Hi")
testPrint("Hello")
testPrint("Bye")


# Задание 2
def logDecorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if args:
            print(f'Function Name: {func.__name__}')
            print(f'Arguments: {args}', end='')
        else:
            print(f'Function Name: {func.__name__}')
            print('Arguments: None', end='')
        if kwargs:
            print(f', {kwargs}')
        else:
            print('')
        if result is not None:
            print(f'Result: {result}')
        else:
            print('Result: None')
        return result

    return wrapper


@logDecorator
def testText(t):
    return t


print(testText("Hello, world!"))
print(testText("Hi"))
print(testText("Hello"))


# Задание 3
def authorization_check(login, password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if login and password:
                return func(*args, **kwargs)
            else:
                print("Ошибка, требуется аутентификация")

        return wrapper

    return decorator


login = input("Введите логин: ")
password = input("Введите пароль: ")


@authorization_check(login, password)
def test_text(t):
    return t


print(test_text('Авторизация успешна'))


# Задание 4
def checkArg(arg, result):
    def outWrapper(func):
        def inWrapper(*args, **kwargs):
            if args:
                for i in args:
                    if not any(isinstance(i, t) for t in arg):
                        print("Ошибка по аргументам")
                        return None
            elif kwargs:
                for i in kwargs.values():
                    if not any(isinstance(i, t) for t in arg):
                        print("Ошибка по аргументам")
                        return None
            resu = func(*args, **kwargs)
            if any(isinstance(resu, t) for t in result):
                return resu
            else:
                print("Ошибка в типе результата функции")
                return None

        return inWrapper
    return outWrapper


arg = [int, str]
res = [int, str]


@checkArg(arg, res)
def testCheckArg(x, y):
    return str(x) * y


print(testCheckArg(4, 2))


# Задание 5 доп
def cashFunc(func):
    cashList = []

    def outWrapper(*args, **kwargs):
        print(cashList)
        key = (args, frozenset(kwargs.items()))

        for item in cashList:
            if item[0] == key:
                print("Результат получен из кэша")
                return item[1]

        result = func(*args, **kwargs)
        cache_entry = (key, result)
        cashList.append(cache_entry)
        print("Результат сохранён в кэш")

        if len(cashList) > 3:
            cashList.pop(0)

        return result

    return outWrapper


@cashFunc
def uppInter(x):
    temp = 0
    for i in range(x):
        temp = i * x
    return temp


print(uppInter(67))
print(uppInter(667))
print(uppInter(67))
print(uppInter(679))







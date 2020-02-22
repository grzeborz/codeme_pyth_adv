def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def kwadrat(a):  # nowa funkcja, jeden parametr
    return a ** 2


def use_a_function(func, *args):
    # debug
    print('"args" zawiera:', args)

    name = func.__name__
    result = func(*args)

    if len(args) == 1:
        print(f'{args[0]} {name} = {result}')
    if len(args) == 2:
        print(f'{args[0]} {name} {args[1]} = {result}')
    return result


if __name__ == '__main__':
    use_a_function(add, 5, 7)
    use_a_function(kwadrat, 11)

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def use_a_function(func, a, b):
    name = func.__name__
    result = func(a, b)
    print(f'{a} {name} {b} = {result}')
    return result


if __name__ == '__main__':
    use_a_function(subtract, 11, 17)

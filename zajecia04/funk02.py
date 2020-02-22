def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


if __name__ == '__main__':
    list_of_functions = [add, subtract, multiply, divide]

    chosen_function = list_of_functions[1]

    name = chosen_function.__name__
    print(name)

    a = 31
    b = 7
    result = chosen_function(a, b)
    print(f'{a} {name} {b} = {result}')

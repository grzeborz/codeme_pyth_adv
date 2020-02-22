def verbose_addition(a, b):
    result = a + b
    print(f'{a} + {b} = {result}')
    return result


if __name__ == '__main__':
    function = verbose_addition  # uwaga, nie ma nawiasów!

    print(type(function))

    result = function(13, 17)

    print(result)

    print("Czy to jest ten sam obiekt?", function is verbose_addition)

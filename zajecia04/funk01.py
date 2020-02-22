def verbose_addition(a, b):
    result = a + b
    print(f'{a} + {b} = {result}')
    return result


if __name__ == '__main__':
    result = verbose_addition(13, 17)
    print(result)

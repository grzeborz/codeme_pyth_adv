# przykład ze zwracaniem wartości z dekoratora

def result_times_100(f):
    def wrapper():
        result = f()
        return result * 100

    return wrapper


@result_times_100
def return_13():
    number = 13
    return number


if __name__ == '__main__':
    print(return_13())

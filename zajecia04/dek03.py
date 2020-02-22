import random
import time


def frame(function):
    def wrapper():
        print('-----------------------------------')
        function()
        print('-----------------------------------')

    return wrapper


def frame2(function):
    def wrapper():
        print('===================================')
        function()
        print('===================================')

    return wrapper


@frame
@frame2
def calculations():
    # ta funkcja nie robi nic pożytecznego
    print('liczę', end='')
    for _ in range(5):
        print('.', end='', flush=True)
        time.sleep(0.5)
    print('obliczyłem! wynik to: ', random.randint(10, 100))


if __name__ == '__main__':
    calculations()
    print()  # oddzielenie pustą linią
    calculations()
    print()
    calculations()

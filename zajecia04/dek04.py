import random
import time


def frame(function):
    def wrapper(trudnosc):
        print('-----------------------------------')
        function(trudnosc)
        print('-----------------------------------')

    return wrapper


@frame
def calculations(trudnosc=5):
    # ta funkcja nie robi nic pożytecznego
    print('liczę', end='')
    for _ in range(trudnosc):
        print('.', end='', flush=True)
        time.sleep(0.5)
    print('obliczyłem! wynik to: ', random.randint(10, 100))


if __name__ == '__main__':
    calculations(10)
    print()  # oddzielenie pustą linią
    calculations(7)
    print()
    calculations(2)

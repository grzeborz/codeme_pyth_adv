# tutaj wpisz swoje imię i nazwisko

from datetime import datetime
from datetime import time
import random
import time


def timer(function):
    years = datetime.now().year
    months = datetime.now().month
    days = datetime.now().day
    hours = datetime.now().hour
    minutes = datetime.now().minute
    seconds = datetime.now().second
    time_start = datetime(years, months, days, hours, minutes, seconds)

    years = datetime.now().year
    months = datetime.now().month
    days = datetime.now().day
    hours = datetime.now().hour
    minutes = datetime.now().minute
    seconds = datetime.now().second
    time_end = datetime(years, months, days, hours, minutes, seconds)
    delta = time_end - time_start
    return delta#timeofprocess
    # return years

@timer
def example_function(trudnosc=10):
    for _ in range(trudnosc):
        print('.', end='', flush=True)
        time.sleep(random.uniform(0, 0.1))
    print()


if __name__ == '__main__':
    timer(example_function)
    print(timer(example_function))
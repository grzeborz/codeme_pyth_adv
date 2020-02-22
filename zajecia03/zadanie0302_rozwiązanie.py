# etap 1

numbers = [74.59, 52.812, 41.329, 23.323, 78.828, 74.6, 49.828, 3.685, 88.161, 62.02]

rounded = [round(x, 1) for x in numbers]
print(rounded)

# etap 2
from countries import countries

countries_starting_with_m = [name for name in countries if name[0] == 'M']
print(countries_starting_with_m)

# etap 3

numbers = [74.59, 52.812, 41.329, 23.323, 78.828, 74.6, 49.828, 3.685, 88.161, 62.02]

polish_numbers = [str(x).replace('.', ',') for x in numbers]
print(polish_numbers)

# etap 4

import random

random_numbers = [random.randint(0, 100000) / 1000 for x in range(10)]
print(random_numbers)

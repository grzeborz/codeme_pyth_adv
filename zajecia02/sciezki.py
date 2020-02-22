# dokumentacja tutaj: https://docs.python.org/3/library/pathlib.html

import pathlib

directory = pathlib.Path()

print(directory)
print(directory.absolute())

new_directory = directory / 'nowy_katalog'  # przeciążony operator "/"

print(new_directory)
print(new_directory.absolute())

print(f'Czy "{new_directory}" istnieje? {new_directory.exists()}')

# poniższa linijka stworzy katalog
new_directory.mkdir()

print(f'Czy "{new_directory}" istnieje? {new_directory.exists()}')

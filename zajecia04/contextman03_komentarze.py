import pathlib


class TempDir:
    """Creates a temporary directory to store temporary files"""

    def __init__(self, path: str):
        self.path = pathlib.Path(path)

    def __enter__(self):
        self.path.mkdir(exist_ok=True)  # tworzenie katalogu `self.path`
        return self.path  # to jest ta sama wartość, która nazwana jest `path` w linii 21

    def __exit__(self, exc_type, exc_val, exc_tb):
        for f in self.path.iterdir():
            f.unlink()  # kasowanie pliku `f`
        self.path.rmdir()  # kasowanie katalogu `self.path`


if __name__ == '__main__':
    with TempDir('temp_dir') as path:
        # w tym bloku tworzymy dziesięć plików w katalogu `path`
        for i in range(10):
            f = path / f'file_{i}.temp'
            f.touch()  # tworzenie pliku `f`

        input('press Enter')  # skrót w PyCharmie do przeładowania podglądu plików: ctrl + alt + y

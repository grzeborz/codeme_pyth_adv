import pathlib


class TempDir:
    """Creates a temporary directory to store temporary files"""

    def __init__(self, path: str):
        self.path = pathlib.Path(path)

    def __enter__(self):
        self.path.mkdir(exist_ok=True)
        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        for f in self.path.iterdir():
            f.unlink()
        self.path.rmdir()


if __name__ == '__main__':
    with TempDir('temp_dir') as path:

        for i in range(10):
            f = path / f'file_{i}.temp'
            f.touch()

        input('press Enter')

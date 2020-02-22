class ColouredText:
    bcolors = {
        'HEADER': '\033[95m',
        'OKBLUE': '\033[94m',
        'OKGREEN': '\033[92m',
        'WARNING': '\033[93m',
        'FAIL': '\033[91m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m'
    }

    def __init__(self, colour='HEADER'):
        self.colour = self.bcolors[colour]

    def __enter__(self):
        print(self.colour, end='')

    def __exit__(self, *args):
        print('\033[0m', end='')


if __name__ == '__main__':
    with ColouredText('OKGREEN'):
        print('hej!')

    print('hej!')

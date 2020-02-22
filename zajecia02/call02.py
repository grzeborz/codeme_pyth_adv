class FramedText:
    def __init__(self, text):
        self.text = text

    def __call__(self, char='*'):
        line = char * (len(self.text) + 4)
        line_with_text = f'{char} {self.text} {char}'
        return f'{line}\n{line_with_text}\n{line}'


if __name__ == '__main__':
    ft = FramedText('Beautiful is better than ugly')
    print(ft())
    print()
    print(ft('#'))

    print()
    # nadal mamy dostęp do atrybutów
    print(ft.text)

class FramedText:
    def __init__(self, text):
        self.text = text

    def give_framed_text(self, char='*'):
        line = char * (len(self.text) + 4)
        line_with_text = f'{char} {self.text} {char}'
        return f'{line}\n{line_with_text}\n{line}'


if __name__ == '__main__':
    ft = FramedText('Beautiful is better than ugly')
    print(ft.give_framed_text())
    print()
    print(ft.give_framed_text('#'))

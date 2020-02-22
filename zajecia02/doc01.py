class FramedText:
    """
    A simple class that puts the text in a frame
    """

    def __init__(self, text):
        self.text = text

    def __call__(self, char='*'):
        """
        Returns the text in a frame
        :param char: a character used to make the frame
        :return: the text in the frame
        """

        line = char * (len(self.text) + 4)
        line_with_text = f'{char} {self.text} {char}'
        return f'{line}\n{line_with_text}\n{line}'


if __name__ == '__main__':
    ft = FramedText('Beautiful is better than ugly')
    # print(ft())
    help(ft)

    print(ft.__doc__)

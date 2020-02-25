# tutaj wpisz swoje imię i nazwisko
import random

class Deck:
    def __init__(self):
        self._cards = ['2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠', '2♣', '3♣', '4♣',
                       '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥',
                       '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦',
                       'J♦', 'Q♦', 'K♦', 'A♦']

    def __iter__(self):
        """
        Function that returns itself
        :return:
        """
        return self

    def __next__(self):
        """
        Function that returns random card
        :return:
        """

        dont_touch = []

        if len(self._cards) <= 0 or len(self._cards) == None:
            raise StopIteration
        else:
            n = random.randrange(len(self._cards))
            dont_touch.append(self._cards[n])
            self._cards.pop(n)
            return dont_touch[-1]


if __name__ == '__main__':
    # tutaj można pisać dowolny kod, nie wpływa to na testy
    deck = Deck()
    for card in deck:
        print(card)
    print(next(Deck()))
    print(Deck())

    pass

# tutaj wpisz swoje imię i nazwisko

from zaddom02_e1_grzechu import Deck


def draw_cards(deck, amount=1):
    # card_list = []
    deck = Deck()
    return deck
    # pass


if __name__ == '__main__':
    deck = Deck()
    print(deck)
    player1 = draw_cards(deck, 14)
    player2 = draw_cards(deck, 14)
    player3 = draw_cards(deck, 14)
    player4 = draw_cards(deck, 14)

    print(player1)
    print(player2)
    print(player3)
    print(player4)

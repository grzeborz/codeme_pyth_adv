# tutaj wpisz swoje imię i nazwisko

from zaddom02_e1_grzechu import Deck


def draw_cards(deck, amount=1):

    card_list = []
    for i in range(amount):
        elo = next(deck)
        if elo != None:
            card_list.append(elo)
        else:
            card_list.append(' ')
        # amount -= 1
    # deck = card_list
    return card_list
    # pass


if __name__ == '__main__':
    deck = Deck()
    # print(draw_cards(deck, 12))

    player1 = draw_cards(deck, 14)
    player2 = draw_cards(deck, 14)
    player3 = draw_cards(deck, 14)
    player4 = draw_cards(deck, 14)

    print(player1)
    print(player2)
    print(player3)
    print(player4)

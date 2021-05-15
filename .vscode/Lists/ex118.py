from random import *
def createDeck():
    length = 0
    Deck = list()
    cardgen = ''
    suits = ['h','d','s','c']
    values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    while length != 52:
        cardgen = f'{values[randint(0,12)]}{suits[randint(0,3)]}'
        if cardgen not in Deck:
            Deck.append(cardgen)
            length = len(Deck)
    return Deck

print(createDeck())
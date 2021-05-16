from ex118 import createDeck
def deal(deck):
    temp = list()
    cardlist = list()
    for i in range(4):
        for f in range(5):
            temp.append(deck[f])
            deck.pop(f)
        cardlist.append(temp)
    return cardlist, deck

print(deal(createDeck()))

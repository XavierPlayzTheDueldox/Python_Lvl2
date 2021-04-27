from random import randint

def rand_lot():
    newlist = list()
    while len(newlist) != 6:
        add = randint(1,49)
        if not add in newlist:
            newlist.append(add)
    return sorted(newlist)


print(*rand_lot(), sep=' ')
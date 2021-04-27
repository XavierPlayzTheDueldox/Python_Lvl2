from random import randint

def rand_lot():
    newlist = list()
    while len(newlist) != 6:
        add = randint(1,49)
        if not add in newlist:
            newlist.append(add)
    return sorted(newlist)

print("")
print('===LOTTERY NUMBER WINNERS===')
print(' ', end="")
print(*rand_lot(), sep='   ')
print('============================')
print("")
print("Did you win the Lottery?")
print("")
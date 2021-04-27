#Ex 120 Is a List already in Sorted Order?
def readlist(lis):
    return sorted(lis)

numberslist = list()
    ans = input('Enter your list inputs')
    while ans != 0:
        numberslist.append(ans)
        ans = input(msg)
if readlist(numberslist) == numberslist:
    return True
else:
    return False
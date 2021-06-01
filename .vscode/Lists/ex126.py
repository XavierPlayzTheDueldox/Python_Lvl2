from random import *
from ex125 import *
def genSublist(listinp):
    sublists = [[],listinp]
    for i in range(len(listinp)):
        sublists.append(list(listinp[i]))
    ll = len(listinp)
    ssl = []
    reqlen = ll + 2 + ((ll * (ll-1))/2)+1
    while len(sublists) != reqlen:
        for i in range(randint(2,(ll-1))):
            ssl.append(listinp[randint(0,ll-1)])
        if isSublist(ssl,listinp):
            sublists.append(ssl)


#len -> 3, conseg -> 2         2    3
#len -> 4, conseg -> 2+3       7    6
#len -> 5, conseg -> 2+3+4     11   10
#len -> 6, conseg -> 2+3+4+5   16   15
#len -> 7, conseg -> 2+3+4+5+6 22   21 ((nxn-1)/2)+1
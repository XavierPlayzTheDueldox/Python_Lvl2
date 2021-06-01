def primedetect(limit):
    allnum = []
    for i in range(limit):
        allnum.append(i)
    allnum.pop[0]
    allnum.pop[1]
    p = 2
    cross = p+2
    while p < limit:
        allnum.pop[cross]
        cross += 2
    return allnum

limit = int(input('Enter the limit:'))
print(primedetect(limit))
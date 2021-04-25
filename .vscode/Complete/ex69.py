a = 2
b = 3
c = 4
pi = 3
print(pi)

for i in range(1000000):
    pi = pi + (4 / (a * b * c))
    a += 2
    b += 2
    c += 2
    print(pi)

    pi = pi - (4 / (a * b * c))
    a += 2
    b += 2
    c += 2
    print(pi)


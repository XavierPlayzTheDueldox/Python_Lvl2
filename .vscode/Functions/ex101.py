def fraction_simplify(m,n):
    d=min(m,n)
    while (m%d)!=0 or (n%d)!=0:
        d-=1
    return m//d, n//d


m = int(input('Enter a number:'))
n = int(input('Enter a second number:'))
print(fraction_simplify(m,n))
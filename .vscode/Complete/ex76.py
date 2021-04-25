n = float(input(" Please Enter the value n: "))
factor = 2
while factor <= n:
    if (n % factor) == 0 :
        print(factor)
        n = n / factor
    else:
        factor += 1
from random import *

n = randint(0, 36)

if n == 0:
    print('Pay 0')

else:
    s = n
    if n == 1 or n == 3 or n == 5 or n == 7 or n == 9 or n == 12 or n == 14 or n == 16 or n == 18 or n == 19 or n == 21 or n == 23 or n == 25 or n == 27 or n == 30 or n == 32 or n == 34 or n == 36:
        br = 'Red'
    else:
        br = 'black'
    
    if n % 2 != 0:
        typ = 'Odd'
    else:
        typ = 'Even'

    
    if n >= 1 and n <= 18:
        f = '1 to 18'
    else:
        f = '19 to 36'


    print(f'The spin resulted in {n}...')
    print(f'Pay {s}')
    print(f'Pay {br}')
    print(f'Pay {typ}')
    print(f'Pay {f}')
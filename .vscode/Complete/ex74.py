print('  ', end="")
for h in range(10):
    print(f'{(h+1):>4d}', end="")
    
print('')
for i in range(10):
    print(f'{(i+1):>2d}', end="")
    for k in range(10):
        print(f'{((i+1)*(k+1)):>4d}', end="")
    print('')


ans = 'no u'
total = 0

while ans != '':
    ans = input('Enter the price: (Blank to exit)')
    if ans == '':
        break
    ans = float(ans)
    total = total + ans

print(f'Card Payment Price: ${total:.2f}')

pennies = total * 100
pennies = pennies // 5
pennies = pennies * 5
pennies = pennies / 100

print(f'Cash Payment: ${pennies:.2f}')
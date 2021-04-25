ans = 'no u'
total = 0

while ans != '':
    ans = input('Enter the price: (Blank to exit)')
    if ans == '':
        break
    ans = float(ans)
    total = total + ans

print(f'Card Payment Price: ${total:.2f}')

pennies = int(total * 100)

for i in range(3):
    pennies -= 1
    if pennies % 5 == 0:
        break

while pennies % 5 != 0:
    pennies += 1

pennies = pennies / 100

print(f'Cash Payment: ${pennies:.2f}')
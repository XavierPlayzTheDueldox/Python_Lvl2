binary = input('enter a number: ')
decimal = 0
for digit in binary:
    decimal = decimal * 2 + int(digit)

print (f'This is the decimal: {decimal}')
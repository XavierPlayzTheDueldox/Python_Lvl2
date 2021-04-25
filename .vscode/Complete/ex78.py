number = int(input('Enter a Decimal to Convert to a Binary:'))
base = 2
remainder = 6
binary = str()

while number >= 2:
    if number % 2 == 1:
        binary = '1' + binary
    else: 
        binary = '0' + binary
    number = number // 2

final = number%base
if final % 2 == 1:
    binary = '1' + binary
else:
    binary = '0' + binary

print(f'The binary is {binary}.')
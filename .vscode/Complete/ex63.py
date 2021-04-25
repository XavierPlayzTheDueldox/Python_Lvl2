currenttemp = 0

print(f'{"CELSIUS":=^24}' + f'{"FAHRENHEIT":=^24}')

for i in range(10):
    currenttemp += 10
    print(f'{currenttemp:^24}' + f'{int(currenttemp * 9/5 + 32) :^24}')

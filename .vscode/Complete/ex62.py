normprice = 4.95
discprice = f'{normprice * 0.6:.2f}'

print(f'{"NORMAL PRICE":=^24}' + f'{"DISCOUNTED PRICE":=^24}')

for i in range(5):
    print(f'{normprice :^24}' + f'{discprice :^24}')
    normprice += 5
    discprice = f'{normprice * 0.6:.2f}'
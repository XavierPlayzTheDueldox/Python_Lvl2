age = 'hi'
total = 0

while age != '':
    age = input('Enter your age:')
    if age == '':
        break
    age = int(age)
    if age < 3:
        total += 0
    elif age < 13 :
        total += 14
    elif age < 65:
        total += 23
    else:
        total += 18
    print(total)

print(f'The total cost of your admission fees is ${total}.')

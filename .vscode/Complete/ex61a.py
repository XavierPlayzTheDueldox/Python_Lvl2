num = float(input('Enter a number:'))
total, count = 0, 0

while num != 0:
    count += 1
    total += num
    num = float(input('Enter a number:'))

if count > 0:
    print(f'The Average of your {count} number(s) is {total / count}.')
else:
    print('You have exited without entering a number. No Average for you.')
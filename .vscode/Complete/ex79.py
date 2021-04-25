from random import randint
max_int = randint(1, 100)
prev_int = 0
new_int = 0
number_of_updates = 0

print('<========== Welcome to the MIG! ==========>')
print(max_int)

for i in range(99):
    new_int = randint(1, 100)
    if new_int > max_int:
        print(new_int, '==> Update')
        max_int = new_int
        number_of_updates += 1
    else:
        print(new_int)

print(f'Total number of updates: {number_of_updates}')
print(f'Maximum Integer: {max_int}')

print('<======= Thanks for using the MIG! =======>')

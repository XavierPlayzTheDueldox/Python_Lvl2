from ex85a import ordinal

def verse(n):
    print(f'On the {ordinal(n)} day of Christmas my true love gave to me,')
    if n >= 12:
        print('Twelve Drummers Drumming,')
    if n >= 11:
        print('Eleven Pipers Piping,')
    if n >= 10:
        print('Ten Lords-a-Leaping,')
    if n >= 9:
        print('Nine ladies Dancing,')
    if n >= 8:
        print('Eight Maids-a-Milking,')
    if n >= 7:
        print('Seven Swans a-Swimming,')
    if n >= 6:
        print('Six Geese a-Laying,')
    if n >= 5:
        print('Five Gold Rings,')
    if n >= 4:
        print('Four Calling Birds,')
    if n >= 3:
        print('Three French Hens,')
    if n >= 2:
        print('Two Turtle Doves,')
    if n == 1:
        print('A Partridge in a Pear Tree.')
    else:
        print('And a Partridge in a Pear Tree.')
    print('')


for i in range(12):
    verse(i+1)


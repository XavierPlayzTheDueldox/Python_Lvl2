x1 = int(input('Enter the x coordinate:'))
y1 = int(input('Enter the y coordinate:'))
x2 = 0
x = x1
y = y1
total = 0
while x2 != '':
    x2 = input('Enter the x coordinate: (Blank to Quit)')
    if x2 == '':
        break
    y2 = int(input('Enter the y coordinate:'))
    x2 = int(x2)
    distance = (((y2 - y)*(y2 - y)) + ((x2 - x)*(x2 - x))) ** (1/2)
    total = total + distance
    x = x2
    y = y2

total = int(total) + (((y2 - y1)*(y2 - y1)) + ((x - x1)*(x - x1))) ** (1/2) 
print(f'The perimeter of the polygon is {total}.')

grade = 'Hello'
total = 0
count = 0

while grade != '':
    grade = input('Enter a grade:')
    if grade == 'A+' or grade == 'A':
        total += 4
    elif grade == 'A-':
        total += 3.7
    elif grade == 'B+':
        total += 3.3
    elif grade == 'B':
        total += 3
    elif grade == 'B-':
        total += 2.7
    elif grade == 'C+':
        total += 2.3
    elif grade == 'C':
        total += 2
    elif grade == 'C-':
        total += 1.7
    elif grade == 'D+':
        total += 1.3
    elif grade == 'D':
        total += 1
    else:
        total += 0

    count += 1


print(f'The average grade points is {total / count}.')

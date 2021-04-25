def median(no1, no2, no3):
    if no1 <= no2 and no1 >= no3 or no1 <= no3 and no1 >= no2:
        return no1
    elif no2 <= no1 and no2 >= no3 or no2 <= no3 and no2 >= no1:
        return no2
    elif no3 <= no1 and no3 >= no2 or no3 <= no2 and no3 >= no1 :
        return no3

no1 = float(input('Enter your first number:'))
no2 = float(input('Enter your second number:'))
no3 = float(input('Enter your third number:'))

print(f'The median of the three numbers is {median(no1, no2, no3)}.')

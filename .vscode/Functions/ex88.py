def triangle_check(no1,no2,no3):
    if no1+no2<=no3 or no2+no3<=no1 or no1+no3<=no2:
        return False
    else:
        return True

no1 = int(input('Enter side 1 of Triangle'))
no2 = int(input('Enter side 2 of Triangle'))
no3 = int(input('Enter side 3 of Triangle'))
print(triangle_check(no1,no2,no3))
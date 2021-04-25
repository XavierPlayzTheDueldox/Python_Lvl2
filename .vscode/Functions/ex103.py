from ex100 import days_in_a_month
from ex92 import prime

def magic_dates():
    day = 1
    month = 1
    year = 1900
    subyear = 0
    while year != 2000:
        if not prime(subyear) and subyear != 0:
            if day * month == subyear:
                print(f'{day}/{month}/{year}')
            day += 1
            if month >= 12:
                month = 1
                year += 1
                subyear += 1
            if day >= days_in_a_month(month,year):
                day = 1
                month += 1
        else:
            if subyear <= 31 and subyear != 0:
                if subyear <= 11:
                    print(f'1/{subyear}/{year}')
                print(f'{subyear}/1/{year}')
            year += 1
            subyear += 1

magic_dates()
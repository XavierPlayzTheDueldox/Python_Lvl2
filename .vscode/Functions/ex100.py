def days_in_a_month(month, year):
    days = [31,0,31,30,31,30,31,31,30,31,30,31]
    if month >= 1 and month <= 12:
        if days[month-1] != 0:
            return days[month-1]
        else:
            if year % 400 == 0:
                return 29
            elif year % 100 == 0:
                return 28
            elif year % 4 == 0:
                return 29
            else:
                return 28
    else:
        return None

if __name__ == '__main__':
    month = int(input('Enter the month:'))
    year = int(input('Enter the year:'))
    print(days_in_a_month(month,year))
MONTH_DAYS = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
YEAR = 1900
SUNDAYS = 0

def get_feb_days():
    global YEAR
    if YEAR % 4 > 0:
        return 28
    elif YEAR % 100 > 0:
        return 29
    elif YEAR % 400 > 0:
        return 28
    return 29

def get_num_sundays():
    global MONTH_DAYS
    global YEAR
    global SUNDAYS
    remainds = 0
    for years in range(1900, 2001):
        for month in range(len(MONTH_DAYS)):
            days = MONTH_DAYS[month]
            if month == 1:
                days = get_feb_days()
            remainds = (days + remainds) % 7
            if years > 1900 and remainds == 6:
                SUNDAYS += 1

if __name__ == '__main__':
    get_num_sundays()
    print SUNDAYS


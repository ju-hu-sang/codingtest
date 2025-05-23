def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def days_in_month(month, year):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_months[1] = 29
    
    return days_in_months[month - 1]

def count_days(day, month, year):
    days_count = 0
    for m in range(1, month):
        days_count += days_in_month(m, year)
    days_count += day
    
    return days_count

while True:
    day, month, year = map(int, input().split())

    if day == 0 and month == 0 and year == 0:
        break
    print(count_days(day, month, year))

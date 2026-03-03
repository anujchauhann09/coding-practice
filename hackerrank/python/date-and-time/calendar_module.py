import calendar

month, day, year = map(int, input().split())

day_number = calendar.weekday(year, month, day)
day = calendar.day_name[day_number]
print(day.upper())
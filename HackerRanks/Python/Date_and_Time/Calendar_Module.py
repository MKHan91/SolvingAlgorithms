import calendar

calendar_input = input().split(" ")
month, day, year = int(calendar_input[0]), int(calendar_input[1]), int(calendar_input[2])
weekday = calendar.weekday(year, month, day)
print((list(calendar.day_name)[weekday]).upper())

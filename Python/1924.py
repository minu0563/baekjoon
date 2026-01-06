import datetime

month, day = map(int, input().split())
date = datetime.date(2007, month, day)

weekday_index = date.weekday()
weekdays = ["MON", 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
print(weekdays[weekday_index])
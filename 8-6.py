from datetime import date
day_now = date.today()
print(day_now)

xday = date(2012, 8, 13)
td = day_now - xday
print(td)

from datetime import datetime
now = datetime.today()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

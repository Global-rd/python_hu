from datetime import datetime as dt
from datetime import timezone, timedelta
now = dt.now(timezone.utc)
print(now)

# STRING TO DATE
date_string = "2023-10-11 15:30:45"
date_object = dt.strptime(date_string, "%Y-%m-%d %H:%M:%S")
#https://www.programiz.com/python-programming/datetime/strptime
print(type(date_object))

# DATE TO STRING

date_string = dt.strftime(date_object, "%Y-%m-%d %H*%M*%S")

# adding day differences to dates

five_days = timedelta(days=5)
new_date = now + five_days
print(new_date)
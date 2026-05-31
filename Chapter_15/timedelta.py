import datetime

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
#(11,36548, 0)
print(delta.total_seconds())
#986948.0
print(str(delta))
#'11 days, 10:09:08'

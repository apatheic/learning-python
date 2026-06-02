import datetime

print(datetime.datetime.now())
dt = datetime.datetime(2015, 10, 30, 15, 29, 0)
print(dt.year, dt.day, dt.month)

print(dt.hour, dt.minute, dt.second)

dt.fromtimestamp(1000000)
dt.fromtimestamp(time.time())

datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
#datetime.datetime(2015, 10, 21, 0, 0)
datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
#datetime.datetime(2015, 10, 21, 16, 29)
datetime.datetime.strptime("October of '15", "%B of %y")
#datetime.datetime(2015, 10, 1,0,0)
datetime.datetime.strptime("November of '63", "%B of '%y")
#datetime.datetime(2063, 11, 1, 0, 0)

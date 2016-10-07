from datetime import datetime
now = datetime.now()
print(now)
print(type(now))

dt=datetime(2016,10,21,10,10,29)
print(dt)
print(now.timestamp())
print(datetime.fromtimestamp(now.timestamp()))
# d = datetime.strptime("2011-10-21 10:10:25", "%Y-%d-%m %H:%M:%S")
# print(d)


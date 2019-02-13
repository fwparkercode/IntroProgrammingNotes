import datetime

birthdate = datetime.datetime(2000, 1, 1, 12, 0, 0)
now = datetime.datetime.now()

age = now - birthdate
print(age.days)

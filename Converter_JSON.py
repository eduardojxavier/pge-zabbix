import datetime
import time

diaIni = 29
mesIni = 2
anoIni = 2024

date_time = datetime.datetime(anoIni, mesIni, diaIni, 23,59)

print(date_time)

a = time.mktime(date_time.timetuple())

print(a)
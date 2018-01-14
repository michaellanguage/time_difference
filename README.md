Check time diffence in python
>>> import datetime
>>> date1 = datetime.datetime.now()
>>> date1
datetime.datetime(2018, 1, 13, 21, 17, 58, 988758)
>>> date2 = datetime.datetime.now()
>>> date2
datetime.datetime(2018, 1, 13, 21, 18, 18, 324488)
>>> date1 - date2
datetime.timedelta(-1, 86380, 664270)
>>> difference = date1 - date2
>>> difference.seconds
86380
>>> difference.second
Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
AttributeError: 'datetime.timedelta' object has no attribute 'second'
>>> difference.seconds
86380
import time
from time_difference import time_difference
date1 = datetime.datetime.now()
time.sleep(1)
date2 = datetime.datetime.now()
difference= time_difference(date1,date2)
print(difference.seconds)#1
print(difference.any)#any time difference bool true/false
print(difference.totaltime)

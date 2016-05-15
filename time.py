import time
import calendar

print (time.time())
local_time =  time.asctime(time.localtime(time.time()))
cal = calendar.month(2008,1)
print (local_time)
print (cal)

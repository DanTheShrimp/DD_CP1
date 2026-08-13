#DD Period 7 just time notes

import time
import datetime

epoch = time.time()
readable_time = time.ctime(epoch)

print(f"The time in seconds since January 1, 1970 is {epoch}")
print(f"A more readable time is {readable_time}")

now = datetime.datetime.now()
hour = now.hour
minute = now.minute
second = now.second

print(f"The current time is {now}")
print(f"The current hour is {hour}")
print(f"The current minute is {minute}")
print(f"The current second is {second}")

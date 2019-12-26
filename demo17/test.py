from datetime import datetime
import re
now_time = '2019-12-26 17:07:09'
s = '15:00'
now_time = re.search('.*?(\d+:\d+:\d+)',now_time)[1]
print(now_time)
print(datetime.strptime(now_time,'%H:%M:%S'))

print(datetime.strptime(s,'%H:%M'))

# print(datetime.strptime(s,'%H%M'))
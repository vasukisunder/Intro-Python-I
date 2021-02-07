import sys
import calendar
from datetime import datetime

cal = calendar.TextCalendar(firstweekday=0)

if len(sys.argv) == 1:
  month = datetime.now().month
  year = datetime.now().year
elif int(sys.argv[1])>0 and len(sys.argv) == 2:
  year = datetime.now().year
  month = int(sys.argv[1])
elif int(sys.argv[1])>0 and int(sys.argv[2])>0:
  year = int(sys.argv[2])
  month = int(sys.argv[1])
else:
  print('provide the month followed by the date')


cal.prmonth(year, month)
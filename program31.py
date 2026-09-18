import calendar
cal = calendar.TextCalendar(calendar.SUNDAY)
y = int(input("Enter Year"))
for i in range(1,13):
    cal.prmonth(y,i)
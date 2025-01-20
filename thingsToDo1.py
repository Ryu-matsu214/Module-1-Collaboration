hour = 1
day = 0
seconds_per_hour = 0
seconds_per_day = 0
div = 0
div1 = 0
second = float(hour) * 60 * 60
seconds_per_hour = float(second)
print(seconds_per_hour)

day = seconds_per_hour * 24
print(int(day))

seconds_per_day = seconds_per_hour * 24

div = float(seconds_per_day) / seconds_per_hour
print (div)

div1 = float(seconds_per_day) // seconds_per_hour
print (div1)




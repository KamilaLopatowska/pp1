from datetime import datetime

time24 = input("Enter the time in 24-hour format (hh:mm): ")
time_obj = datetime.strptime(time24, "%H:%M")
time_12_hour = time_obj.strftime("%I:%M %p")
print("Time in 12-hour format: " + time_12_hour)
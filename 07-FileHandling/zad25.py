import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C"

temperatures = re.findall("\d{2}",message) #returns list consisting of strings ['22', '21', '26']
sum = 0
for i in range (0, len(temperatures)):
    temperatures[i] = int(temperatures[i])
    sum = sum + temperatures[i]

mean = sum / len(temperatures)
print(mean)
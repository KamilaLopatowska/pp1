a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")
s = (float(a) + float(b) + float(c))/2
area = (float(s) * (float(s)-float(a)) * (float(s)-float(b)) * (float(s)-float(c))) ** 0.5
circumference = 2 * float(s)
print(f'Triangle area: {area}\n Triangle circumference: {circumference}')
a = int(input("Enter dimension a: "))
b = int(input("Enter dimension b: "))

for i in range(a):
    if i == a - 1 or i == 0:
        print(b * "*")
    else:
        print("*",(b - 2) * "","*")
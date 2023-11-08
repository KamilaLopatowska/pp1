multiply_by = int(input("Enter number: "))
result = 0
for number in range(1,11):
    result = number * multiply_by
    print(f'{multiply_by} x {number} = {result}')
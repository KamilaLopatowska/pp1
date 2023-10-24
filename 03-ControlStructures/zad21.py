number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

if number1 > number2:
    number1, number2 = number2, number1

# Display the numbers in ascending order
print(f'Numbers in ascending order: {number1, number2}')
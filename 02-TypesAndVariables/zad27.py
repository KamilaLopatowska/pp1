enter_number = input("Enter a number: ")
number_check = bool(float(enter_number) >= -10 and float(enter_number) <= 10)
print(f'Number is in the range <-10,10>: {number_check}')
registration_number = input("Enter vehicle registration number: ")
check = bool(registration_number[0:2] == 'KR')
print(f'Car from Kraków: {check}')
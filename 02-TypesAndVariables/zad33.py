password = str(input("Enter password: "))
password_check = bool(len(password) >= 8)
print(f'Password is valid: {password_check}')
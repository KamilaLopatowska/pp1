enter_height = int(input("Enter your height in cm: "))
enter_weight = int(input("Enter your weight in kg: "))
cm_to_m = enter_height/100
print(f'Your BMI index: {enter_weight/cm_to_m**2}')
correct_weight = bool(enter_weight/cm_to_m**2 > 18.5 and enter_weight/cm_to_m**2 < 25)
print(f'Correct weight: {correct_weight}')
with open("number_power", 'w') as file:
    for i in range(1,11):
        i2 = i ** 2
        i3 = i ** 3
        file.write(f'{i},{i2},{i3}\n')
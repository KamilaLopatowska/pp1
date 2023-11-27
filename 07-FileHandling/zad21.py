with open("numbers.txt", 'w') as file:
    for i in range (1, 51):
        number = i
        i = str(i)
        file.write(f'{i}\n')
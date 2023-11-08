for number in range (1, 31):
    if number % 3 == 0 and number % 5 == 0:
        number = "BINGO"
        print(number)
    elif number % 3 == 0:
        number = "THREE"
        print(number)
    elif number % 5 == 0:
        number = "FIVE"
        print(number)
    else:
        print(number)
EAN13_number = int(input("Enter EAN-13 article number: "))
EAN13_number = str(EAN13_number)
if len(EAN13_number) == 13:
    if EAN13_number[0:3] == "590":
        print("Article number is correct.")
        print("Article manufactured in Poland.")
    else:
        print("Article number is correct.")
        print("Article not manufactured in Poland")
else:
    print("Article number is not correct.")
    
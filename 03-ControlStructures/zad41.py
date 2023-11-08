pin = "0805"
for i in range(3):
    answer = (input("Enter pin:"))
    if answer != pin:
        print("Incorrect...")
    elif answer == pin:
        print("Correct")
        break
    print("Sorry, your payment card has been blocked")
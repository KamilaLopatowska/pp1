a = input("Enter father's income: ")
b = input("Enter mother's income: ")
c = input('Enter number of people in family: ')
total = int(a)+int(b)
perPerson = ((int(a)+int(b))/int(c))
print("Total income: ", total)
print("Income per person: ", perPerson)
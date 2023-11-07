# A tree may be cut down if its diameter is at least 50 cm. 
# Write a program that, based on the circumference of the tree entered from the keyboard, calculates and 
# displays the value True if the tree can be cut down, or display the value False otherwise. Sample result:

circumference = int(input("Podaj obwód pnia: "))
diameter = circumference / 3.14
diameter_check = bool(diameter >= 50)
print(diameter_check)
###
# The computer throws dice. Then, the user then tries to guess the number from dice by entering a number from 1 to 6 from the keyboard. 
# If the user has guessed the number from the dice, the computer displays True. Otherwise, the computer displays False.
###

import random

dice_roll = random.randrange(1,7)
user_guess = int(input("Podaj cyfrę od 1 do 6: "))
result = bool (user_guess >=1 and user_guess <= 6 and dice_roll == user_guess)
print(result)
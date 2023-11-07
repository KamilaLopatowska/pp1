# Write a program that displays the number of dice rolled and the value True if the number rolled is 1 or 6.
import random
dice_roll = random.randrange(1,7)
check = bool(dice_roll == 1 or dice_roll == 6)
print(f'Dice rolled: {dice_roll}\n Special number: {check}')
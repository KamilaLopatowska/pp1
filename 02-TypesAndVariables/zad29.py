# Write a program that displays results of three dice rolls and the sum of dice rolled. Apply a random number generator:
import random

dice1 = random.randrange(1,7)
dice2 = random.randrange(1,7)
dice3 = random.randrange(1,7)
sum = dice1 + dice2 + dice3
print(f'Wyniki to: {dice1}, {dice2}, {dice3}, suma wyników to: {sum}')
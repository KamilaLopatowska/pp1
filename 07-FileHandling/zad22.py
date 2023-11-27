import random
with open("random_numbers.txt", 'w') as file:
   for j in range(50): 
        i = random.randint(100, 1000)
        file.write(f'{i}\n')
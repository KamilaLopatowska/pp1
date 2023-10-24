human_years = int(input("Enter the dog's age in human years: "))

if human_years <= 2:
    dog_years = 10.5 * human_years
else:
    dog_years = 10.5 * 2 + 4 * (human_years - 2)

print(f"The dog's age in dog’s years is {dog_years} years.")
# The price of the product on the price tag is given before and after the discount is applied. 
# Write a program that allows you to enter the product price and discount. Display the product price, discount, discounted product price, 
# and the difference between the product price before and after the discount. Display all prices with two decimal places. Sample result:
# Enter price: 24.72
# Enter discount %: 15
# Price with discount: 21.01
# Reduction: 3.71

price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))
discount_price = price - discount / 100 * price
round_discount_price = float(format(discount_price, ".2f"))
reduction = price - round_discount_price
round_reduction = format(reduction, ".2f")
print(f'Price with discount: {round_discount_price}\nReduction: {round_reduction}')
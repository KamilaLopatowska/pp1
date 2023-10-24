products = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))

if products > 2:
    total_price = (products - 2) * product_price * 0.75 + 2 * product_price
else:
    total_price = products * product_price

print(f"Amount to pay: {total_price}")
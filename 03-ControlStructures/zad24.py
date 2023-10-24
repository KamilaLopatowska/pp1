current_price = 1680.00
previous_price = 2157.00

if current_price <= previous_price - previous_price*0.1:
    print(f'Current product price: {current_price}\n Previous product price: {previous_price}\n Buy the product!!\n Product price reduced by {round((current_price/previous_price)*100)}%')

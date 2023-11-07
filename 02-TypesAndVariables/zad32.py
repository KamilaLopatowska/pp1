amount = float(input("Podaj kwotę: "))
vat = 0.23 * amount
rounded_vat = format(vat,".2f")
print(f'Amount : {amount}\nVAT 23% : {rounded_vat}')
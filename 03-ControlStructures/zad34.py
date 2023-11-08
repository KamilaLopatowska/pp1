
amountStart = int(input("Enter the amount: "))
amount = amountStart
coins5 = 0
coins2 = 0
coins1 = 0

coins5 = amount // 5
amount = amount % 5
coins2 = amount // 2
amount = amount % 2
coins1 = amount // 1
amount = amount % 1
print(f'The amount of PLN {amountStart} in coins:\n5 zł {coins5}\n2 zł {coins2}\n1 zł {coins1}')

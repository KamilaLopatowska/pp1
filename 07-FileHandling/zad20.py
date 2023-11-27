with open("MeatAndFish.txt", "r", encoding = "utf-8") as meat_fish:
    file1 = meat_fish.read()
with open("GrainsAndBread.txt", "r", encoding = "utf -8") as grains_bread:
    file2 = grains_bread.read()
with open("allproducts.txt", 'w', encoding = "utf-8") as all_products:            
    all_products.write(file1)
    all_products.write(file2)
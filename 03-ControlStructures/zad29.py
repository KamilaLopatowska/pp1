washing_product = "jacket"
rinse = True
spin = True
washtime = int(0)
if washing_product == "jacket":
    washtime += 40
    if rinse == 1:
        washtime += 15
    else:
        washtime += 0
    if spin == True:
        washtime += 9
        print(f'washing product: {washing_product}\nrinse: {rinse}\nspin: {spin}\nwashtime: {washtime}')
    else:
        washtime += 0
        print(f'washing product: {washing_product}\nrinse: {rinse}\nspin: {spin}\nwashtime: {washtime}')
if washing_product == "shoes":
    washtime += 20
    if rinse == True:
        washtime += 15
    else:
        washtime += 0
    if spin == True:
        washtime += 9
        print(f'washing product: {washing_product}\nrinse: {rinse}\nspin: {spin}\n washtime: {washtime}')
    else:
        washtime += 0
        print(f'washing product: {washing_product}\nrinse: {rinse}\nspin: {spin}\n washtime: {washtime}')
if washing_product == "underwear":
    washtime += 70
    if rinse == True:
        washtime += 15
    else:
        washtime += 0
    if spin == True:
        washtime += 9
        print(f'washing product: {washing_product}\nrinse: {rinse}\nspin: {spin}\n washtime: {washtime}')
    else:
        washtime += 0
        print(f'washing product: {washing_product}\nrinse: {rinse}\nspin: {spin}\n washtime: {washtime}')

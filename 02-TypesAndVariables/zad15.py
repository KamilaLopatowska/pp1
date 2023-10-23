#### 
# Podaj temperaturę w celsjuszach
temperatura_celsjusz = input("Podaj temperaturę w Celsjuszach: ")
# konwersja temperatury z celsjusza na fahrenheita
temperatura_fahrenheit = int(temperatura_celsjusz) * 1.8 + 32
# konwersja temperatury z celsjusza na kelwina
temperatura_kelwin = int(temperatura_celsjusz) + 273.15
# wyświetlanie wyniku
print(f'{temperatura_celsjusz} stopni celsjusza to {float(temperatura_fahrenheit)} stopni Fahrenheita i {float(temperatura_kelwin)} stopni Kelwina')
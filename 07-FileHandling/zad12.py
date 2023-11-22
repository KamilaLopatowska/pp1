name = "Kamila Łopatowska"
university = "Uniwersytet Ekonomiczny w Krakowie"
field = "InformatykaStosowana"

# write to a file
file = open("student.txt", 'w')
file.write(name+"\n")
file.write(university+'\n')
file.write(field)
file.close()

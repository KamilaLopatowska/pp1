with open("data.txt", 'r', encoding = "utf-8") as source:
    with open('copylines.txt', 'w', encoding = 'utf-8') as copy:
        for line in source:
            copy.write(line)
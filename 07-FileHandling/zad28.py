import re

with open("data.txt", 'r', encoding= "utf-8") as file:
    file = file.read()
    words = re.split("\W", file)
    for i in range(0, len(words)):
        if len(words[i]) >= 6:
            print(words[i])
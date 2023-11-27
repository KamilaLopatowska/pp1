with open("data.txt", "r", encoding="utf-8") as file:
    kopia = file.read()
with open("copy.txt", "w", encoding="utf-8") as copy:
    copy.write(kopia)
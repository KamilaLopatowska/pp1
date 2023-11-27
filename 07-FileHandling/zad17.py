lines_per_iteration = 5
with open("data.txt", 'r', encoding = "utf-8") as file:
    lines = file.readlines()
    for start_index in range(0, len(lines), lines_per_iteration):
        for line in lines[start_index:start_index + lines_per_iteration]:
            print(line.strip())
        input()
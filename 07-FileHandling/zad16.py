lines = 0
file_name = input("Enter file name: ")
file = open(file_name, 'r')
for line in file:
    lines += 1
print(f'File name: {file_name}\nNumber of lines: {lines}')
array =[2,3,7,5,4]

#a the array
print(f'Array:{array}')

#b number of elements 
print(f'no. of elements {len(array)}')

#c first value
print(f'first value {array[0]}')

#d second value
print(f'second value {array[1]}')

#e last value
print(f'last value {array[-1]}')

#f last but one value
print(f'last but one value {array[len(array) - 2]}')

#g sum of the first and last value
print(f'sum of the first and last value {array[0] + array[-1]}')

#h middle value
print(f'middle value {array[len(array)//2]}')

#all array values separated by a single space (use a loop statement)
for i in array:
    print(i," ", end ="")
print()
i = 0
while i <= len(array)//2:
    print(array[i]," ", end ="")
    i += 1
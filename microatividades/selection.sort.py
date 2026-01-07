array = [29, 10, 14, 37, 13, 5, 2, 1, 9, 22, 50, 44, 3, 11, 7]

for i in range(len(array)):
    min_idx = i
    for j in range(i + 1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    
    temp = array[i]
    array[i] = array[min_idx]
    array[min_idx] = temp

print(array)
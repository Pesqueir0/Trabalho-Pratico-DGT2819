def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

numeros = [45, 12, 89, 7, 33, 21, 56, 4, 90, 11, 23, 67, 10, 5, 18]
bubbleSort(numeros)
print(numeros)
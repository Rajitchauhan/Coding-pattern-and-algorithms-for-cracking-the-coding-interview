# insertion sort using python 3

def insertion_sort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key

data = [12,53,1,44,12,34]
insertion_sort(data)
print(data)

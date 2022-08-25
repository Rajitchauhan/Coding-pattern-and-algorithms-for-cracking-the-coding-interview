def swap(a , b , arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def partition(elements , start , end):
    pivot_index = start
    #pivot element is leftmost (begining of array`s element)
    pivot = elements[pivot_index]

    while start < end:
        #increment start untill , pivot is greater than start
        while(start < len(elements) and pivot >= elements[start]):
            start += 1
        #decrement start untill , pivot is less than start
        while(pivot < elements[end]):
            end -= 1
        if start < end :
            #swap them if start is less then end
            swap(start , end , elements)
    # if element of pivot is greater than end than swap this too
    swap(pivot_index , end , elements)
    #  return value of end , BCZ we will use in quick_sort
    return end

def quick_sort(elements , start , end):
    if start < end:
        part = partition(elements , start, end)
        quick_sort(elements , start , part-1) # for left most part of array
        quick_sort(elements , part+1 , end) # for right most part of array
    return elements
#output = [2, 7, 9, 11, 15, 28, 29]

elements = [11,9,29,7,2,15,28]
start = 0
end = len(elements) - 1
print(quick_sort(elements , start , end))

def swap(a , b , arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def partition(elements , start , end):
    pivot_index = 0
    #pivot element is leftmost (begining of array`s element)
    pivot = elements[pivot_index]
    start = pivot_index + 1
    #start is next to pivot element , which should be less than pivot
    end = len(elements) - 1
    #end should be greater than pivot
    while start < end:
        #increment start untill , pivot is greater than start
        while(pivot >= elements[start]):
            start += 1
        #decrement start untill , pivot is less than start
        while(pivot < elements[end]):
            end -= 1
        if start < end :
            #swap them if start is less then end
            swap(start , end , elements)
    # if element of pivot is greater than end than swap this too
    swap(pivot_index , end , elements)
    print(elements)

#output = [7, 9, 2, 11, 29, 15, 28]

elements = [11,9,29,7,2,15,28]
start = 1
end = len(elements) - 1

partition(elements , start , end)

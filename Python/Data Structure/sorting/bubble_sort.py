# binnary sorting

def bubble_sort(Array):
    for x in range(len(Array)):

        for j in range(0 , len(Array) - x - 1):
            if Array[j] > Array[j+1]:

                (Array[j] , Array[j+1]) = (Array[j+1] , Array[j])



Data = [2,3,4,8,1,0,22]
bubble_sort(Data)
print(len(Data))
print(Data)

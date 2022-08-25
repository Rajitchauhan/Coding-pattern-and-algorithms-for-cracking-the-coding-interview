"""
problem : you are given two sorted array ,
  A and B , where A has a large enough buffer at the ennd to hold  B simply ,
  write a method  to merge B into A in sorted order.
"""
def sorted_merge(arrayA ,arrayB  , lastA , lastB):
    # index of last element in arrayA and arrayB
    indexA , indexB = lastA -1 , lastB - 1
    #end of  merge array
    indexMerge =  len(arrayA)  - 1
    while (indexB >= 0):
        if indexA >= 0 and arrayA[indexA] > arrayB[indexB]:
            arrayA[indexMerge] = arrayA[indexA]
            indexA -= 1
        else:
            arrayA[indexMerge] = arrayB[indexB]
            indexB -= 1

        indexMerge -= 1
    return arrayA


#output :: [1, 3, 4, 5, 6]
arrayA = [3,4,6,0,0]
arrayB = [1,5]
lastA , lastB = 3   , 2
print(sorted_merge(arrayA ,arrayB  , lastA , lastB))

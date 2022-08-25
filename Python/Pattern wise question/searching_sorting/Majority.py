"""
problem : find majority elements occaranced in array ,
and check if it is greater than half length of array

input : [1,2,5,7,3,5,5,5,5]
        True
"""
def majority(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    # to get the max key of freq 
    maximum = max(freq , key=freq.get)

    if freq[maximum] > len(arr)//2:
        return maximum
    else:
        return False

arr = [1,2,5,7,3,5,5,5,5]
print(majority(arr))

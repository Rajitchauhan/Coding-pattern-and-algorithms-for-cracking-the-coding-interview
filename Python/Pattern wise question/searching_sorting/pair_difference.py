"""
find pair difference from given array

def findpairs(arr,n,L):
    arr.sort()
    n=len(arr)
    i=0
    j=1
    while i<n and j<n:
        if i!=j and arr[j]-arr[i]==L:
            return arr[j],arr[i]
        elif arr[j]-arr[i]<L:
            j+=1
        else:
            i+=1
    return 0
arr=[5,20,3,2,5,80]
n=len(arr)
L=78
print(findpairs(arr,n,L))
"""

def pair_difference(arr , n , k):
    #arr = sorted(arr)
    arr.sort()
    n = len(arr)

    i  , j = 0 , 1
    while  i < n and j < n:
        if i!=j and arr[j]-arr[i]==L:
            return arr[j] , arr[i]
        elif(arr[j] - arr[i] < k):
            j += 1
        else:
            i += 1
    return False
    return 0
arr=[5,20,3,2,5,80]
n=len(arr)
L=78
print(pair_difference(arr,n,L))

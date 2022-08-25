"""
Task : Partition problem is to determine whether a given set can be partitioned into two subsets such that
 the sum of elements in both subsets is the same.
"""
def equal_partition(arr , n):
    sum = 0
    for i in arr:
        sum = sum + i
    if sum%2 != 0:
        return False
    return subset_sum(arr , sum//2 , n)

def subset_sum(arr ,sum ,  n):
    t = [[False for s in range(sum+1)] for i in range(n+1)]

    for i in range(n+1):
        t[i][0] = True
    for i in range(1 , sum+1):
        t[0][i] = False

    for i  in range(1 , n+1):
        for j in range(1 , sum+1):

            if arr[i-1] > j:
                t[i][j] = t[i-1][j]
            if arr[i-1] <= j:
                t[i][j] = t[n-1][j] or t[n-1][j-arr[i-1]]


    return t[i][j]

arr= [3, 34, 4, 12, 5, 2]
n=len(arr)
print(equal_partition(arr , n))

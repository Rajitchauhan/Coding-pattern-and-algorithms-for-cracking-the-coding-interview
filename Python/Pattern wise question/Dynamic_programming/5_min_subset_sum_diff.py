"""
Partition a set into two subsets such that the difference of subset sums is minimum
task : minimum subset sum difference

Input:  arr[] = {1, 6, 11, 5}
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12
Subset2 = {11}, sum of Subset2 = 11

"""
import sys
def min_subset_sum_diff(arr ,  n):
    sum = 0

    for i in range(len(arr)):
        sum += arr[i]

    t = [[0 for i in range(sum+1)] for i in range(n+1)]

    for i in range(n+1):
        t[i][0] = 1
    for i in range(1 , sum+1):
        t[0][i] = 0

    for i in range(1 ,  n+1):
        for j in range(1 , sum+1):
            if arr[i-1] > j:
                t[i][j] = t[i-1][j]
            if arr[i-1] <=j:
                t[i][j] = t[i-1][j] or t[i-1][j-arr[i-1]]

    diff = sys.maxsize

    for j in range(sum//2 , -1 , -1):
        if t[i][j]==1:
            diff = sum - (2*j)
            break
    return diff

arr = [1, 6, 11, 5]
n=len(arr)
print(min_subset_sum_diff(arr , n))

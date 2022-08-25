"""
Task : Given an array arr[] of length N and an integer X,
 the task is to find the number of subsets with a sum equal to X


Input: arr[] = {1, 2, 3, 3}, X = 6
Output: 3
All the possible subsets are {1, 2, 3},
{1, 2, 3} and {3, 3}

Input: arr[] = {1, 1, 1, 1}, X = 1
Output: 4

"""

def count_subset_sum(arr , sum , n):
    t = [[0 for i in range(sum+1)] for j in range(n+1)]

    for i in range(n+1):
        t[i][0] = 1
    for i in range(1 , sum+1):
        t[0][i] = 0

    for i  in range(1 , n+1):
        for j in range(1 , sum+1):

            if arr[i-1] > j:
                t[i][j] = t[i-1][j]
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j] + t[i-1][j-arr[i-1]]


    return t[n][sum]


arr = [1, 1 , 1 , 1]
sum = 1

n=len(arr)
print(count_subset_sum(arr  , sum , n))

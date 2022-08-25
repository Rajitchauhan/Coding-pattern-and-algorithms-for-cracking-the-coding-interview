"""
Task : find subset sum
Ex :: arr = [2 , 3 , 7 , 8 , 10]
      sum : 11
Explanation :: find a subset from array which should be equal to sum
subset : {} , {2} , {3} , {7} , {8} , {10} , {2,3} , {2,7} , {2,8} , {2,10} , {3,7}, {3,8} , {3,10}.... so on
 {8 , 3} which is equal to given sum.

Question : Given a set of non-negative integers,
 and a value sum, determine if there is a subset of the given set with sum equal to given sum.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.


#Recursion
def subset_sum(arr, Sum , n):
    if n==0:
        return False
    if Sum==0:
        return True

    if (arr[n-1] > Sum):
        return subset_sum(arr , Sum , n-1)

    return subset_sum(arr , Sum-arr[n-1] , n-1) or subset_sum(arr , Sum , n-1)

arr= [3, 34, 4, 12, 5, 2]
Sum = 9
n=len(arr)
print(subset_sum(arr , Sum , n))


#Memoirazation
def subset_sum(arr, Sum , n):
    t = [[-1 for i in range(Sum+1)] for i in range(n+1)]
    if n==0:
        return 0
    if Sum==0:
        return 1

    if t[n][Sum] != -1:
        return t[n][Sum]

    if (arr[n-1] > Sum):
        t[n-1][Sum] = subset_sum(arr ,Sum ,  n-1)
        return t[n-1][Sum]
    else:
        t[n-1][Sum] = subset_sum(arr ,Sum ,  n-1)
        return t[n-1][Sum] or subset_sum(arr , Sum-arr[n-1] , n-1)
"""
#top down
def subset_sum(arr, Sum , n):
    t = [[False for i in range(Sum+1)] for i in range(n+1)]
    # If sum is 0, then answer is true
    for i in range(n + 1):
        t[i][0] = True

    # If sum is not 0 and set is empty,
    # then answer is false
    for i in range(1, Sum + 1):
         t[0][i]= False

    for i in range(1, n + 1):
        for j in range(1, Sum + 1):
            if arr[i-1] > j:
                t[i][j] = t[i-1][j]
            if arr[i-1] <= j:
                t[i][j] = (t[i-1][j] or
                                t[i - 1][j-arr[i-1]])

    # uncomment this code to print table
    # for i in range(n + 1):
    # for j in range(sum + 1):
    # print (subset[i][j], end =" ")
    # print()
    return t[n][Sum]



arr= [3, 34, 4, 12, 5, 2]
Sum = 9
n=len(arr)
print(subset_sum(arr , Sum , n))

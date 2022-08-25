"""
arr : 1 , 1 , 3 , 2
diff : 1
output : 3
explanation : {3-2} , {2-1} , {2-1} total subset is 3
"""
def count_subset_sum_diff(arr , diff , n):
    res = 0
    sum = 0
    for i in arr:
        sum += i
    res = (diff + sum) //2

    return subset_sum(arr , res , n)
def subset_sum(arr , res , n):
    t = [[0 for i in range(res+1)] for j in range(n+1)]

    for i in range(n+1):
        t[i][0] = 1
    for i in range(1 , res+1):
        t[0][i] = 0

    for i  in range(1 , n+1):
        for j in range(1 , res+1):

            if arr[i-1] > j:
                t[i][j] = t[i-1][j]
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j] + t[i-1][j-arr[i-1]]


    return t[n][res]


arr= [1 , 1 , 2 , 3]
diff = 1
n=len(arr)
print(count_subset_sum_diff(arr , diff , n))

"""

Problem Statement
You are given an array/list ‘ARR’ of ‘N’ positive integers and an integer ‘K’.
 Your task is to check if there exists a subset in ‘ARR’ with a sum equal to ‘K’.
Note: Return true if there exists a subset with sum equal to ‘K’. Otherwise, return false.
For Example :
If ‘ARR’ is {1,2,3,4} and ‘K’ = 4, then there exists 2 subsets with sum = 4.
 These are {1,3} and {4}. Hence, return true.

Input Format :
The first line contains a single integer T representing the number of test cases.

The first line of each test case contains two space-separated integers ‘N’ and ‘K’
 representing the size of the input ‘ARR’ and the required sum as discussed above.

The next line of each test case contains ‘N’ single space-separated integers that represent the elements of the ‘ARR’.

Output Format :
For each test case, return true or false as discussed above.
Output for each test case will be printed in a separate line.

Note:
You don’t need to print anything, it has already been taken care of. Just implement the given function.

Constraints:
1 <= T <= 5
1 <= N <= 10^3
0 <= ARR[i] <= 10^9
0 <= K <= 10^3

Time Limit: 1 sec

"""

""" Recursion """

def solve(i , k,  arr):
    if k==0:
        return True
    if(i==0):
        return arr[0] == k
    no = solve(i-1 , k , arr)
    take = False
    if arr[i] <= k:
        take = solve(i-1 , k-arr[i] ,  arr)
    return (no or take)


def subsetSumToK(n, k, arr):
    return solve(n-1 , k , arr

""" Top - Down """

def solve(i , k,  arr   , memo):
    if k==0:
        return True
    if(i==0):
        return arr[0] == k
    if memo[i][k] != -1:
        return memo[i][k]
    no = solve(i-1 , k , arr , memo)
    take = False
    if arr[i] <= k:
        take = solve(i-1 , k-arr[i] ,  arr , memo)
    memo[i][k] = (no or take)
    return memo[i][k]


def subsetSumToK(n, k, arr):
    memo = [[-1 for i in range(k+1)] for j in range(n)]
    return solve(n-1 , k , arr , memo)

""" Bottom up """

def subsetSumToK(n, k, arr):
    dp = [[False for i in range(k+1)] for j in range(n)]
    for i in range(n):
        dp[i][0] = True
    if arr[0] <= k:
        dp[0][arr[0]] = True
    for i in range(1 , n):
        for j in range(1 , k+1):
            no = dp[i-1][j]
            take = False
            if arr[i] <= j:
                take = dp[i-1][j-arr[i]]
            dp[i][j] = take or no
    return dp[n-1][k]


def subsetSumToK(n, k, arr):
    t = [[False for i in range(k+1)] for i in range(n+1)]
    # If sum is 0, then answer is true
    for i in range(n + 1):
        t[i][0] = True

    # If sum is not 0 and set is empty,
    # then answer is false
    for i in range(1, k+ 1):
         t[0][i]= False

    for i in range(1, n + 1):
        for j in range(1, k + 1):
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
    return t[n][k]

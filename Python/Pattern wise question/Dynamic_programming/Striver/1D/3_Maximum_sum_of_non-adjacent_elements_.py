"""

Problem Statement
Suggest Edit
You are given an array/list of ‘N’ integers.
 You are supposed to return the maximum sum of the subsequence
  with the constraint that no two elements are adjacent in the given array/list.
Note:
A subsequence of an array/list is obtained by deleting
 some number of elements (can be zero) from the array/list,
  leaving the remaining elements in their original order.

Input Format:
The first line contains a single integer ‘T’ denoting the number of test cases.

The first line of each test case contains a single integer ‘N’ denoting the number of elements in the array.

The second line contains ‘N’ single space-separated integers denoting the elements of the array/list.

Output Format:
For each test case, print a single integer that denotes the maximum sum of the non-adjacent elements.

Print the output of each test case in a separate line.

Note:
You do not need to print anything; it has already been taken care of. Just implement the given function.

Constraints:
1 <= T <= 500
1 <= N <= 1000
0 <= ARR[i] <= 10^5

Where 'ARR[i]' denotes the 'i-th' element in the array/list.


"""
# Recursion
def  solve(i , nums):
    if(i==0):
        return nums[i]
    if(i<0): return 0
    take = solve(i-2 , nums) + nums[i]
    no = solve(i-1  , nums) + 0
    return max(take , no)
def maximumNonAdjacentSum(nums):
    n = len(nums)
    return solve(n-1 , nums)

# top down
def  solve(i , nums , memo):
    if(i==0):
        return nums[i]
    if(i<0):
        return 0
    if(memo[i] != -1):
        return memo[i]

    take = solve(i-2 , nums , memo) + nums[i]
    no = solve(i-1  , nums , memo) + 0
    memo[i] = max(take , no)
    return  memo[i]
def maximumNonAdjacentSum(nums):
    # Write your code here.
    n = len(nums)
    memo = [-1]*n
    return solve(n-1 , nums , memo)

# Main.
t = int(stdin.readline().rstrip())

while t > 0:

    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))

    t -= 1

# Bottom UP
def maximumNonAdjacentSum(nums):
    # Write your code here.
    n = len(nums)
    dp = [0]*n
    dp[0] = nums[0]
    for i in range(1 , n):
        take = nums[i]
        if i >1:
            take += dp[i-2]
        no = dp[i-1]
        dp[i] = max(take , no)
    return dp[n-1]

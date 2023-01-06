"""

You are given an array (0-based indexing) of positive integers and
 you have to tell how many different ways of selecting the elements
 from the array are there such that the sum of chosen elements is equal to the target number “tar”.

Note:
Two ways are considered different if sets of indexes of elements chosen by these ways are different.

Input is given such that the answer will fit in a 32-bit integer.

For Example:
If N = 4 and tar = 3 and the array elements are [1, 2, 2, 3], then the number of possible ways are:
{1, 2}
{3}
{1, 2}
Hence the output will be 3.

Input Format :
The first line of the input contains an integer, 'T’, denoting the number of test cases.

The first line of each test case will contain two space-separated integers ‘N’ and “tar”,
 denoting the size of the array and the target sum.

The second line of each test case contains ‘N’ space-separated integers denoting elements of the array.

Output Format :
For each test case, print the number of ways that satisfy the condition mentioned in the problem statement.

Print a separate line for each test case.

Note :
You do not need to print anything, it has already been taken care of. Just implement the given function.

Constraints:
1 <= T <= 10
1 <= N <= 100
0 <= nums[i] <= 1000
1 <= tar <= 1000



"""
""" one test case fail """
def solve(i , num , tar , memo):
    if tar == 0:
        return 1
    if i == 0:
        if tar == num[0]:
            return 1
        else:
            return 0
    if memo[i][tar] != -1:
        return memo[i][tar]
    no = solve(i-1, num , tar , memo)
    take = 0
    if num[i] <= tar:
        take = solve(i-1 , num , tar-num[i] , memo)
    memo[i][tar] = (no + take)
    return memo[i][tar]

def findWays(num: List[int], tar: int) -> int:
    # Write your code here.
    n = len(num)
    memo = [[-1 for i in range(tar+1)] for j in range(n)]
    return  solve(n-1 , num , tar , memo)


""" Bottom - up """
def findWays(num: List[int], tar: int) -> int:
    # Write your code here.
    n = len(num)
    dp = [[0 for i in range(tar+1)] for j in range(n)]
    for i in range(n):
        dp[i][0] = 1
    if num[0]<=tar:
        dp[0][num[0]] = 1
    for i in range(1 , n):
        for j in range(1 , tar+1):
            no = dp[i-1][tar]
            take = 0
            if num[i]<=j:
                take = dp[i-1][j]
            dp[i][j] = take + no
    return dp[i-1][tar]

""" Passes all test case """

def solve(i , num , tar , memo):

    if i == 0:
        if tar == 0 and num[0] == 0:
            return 2
        if tar == 0 or num[0] == tar:
            return 1
        return 0
    if memo[i][tar] != -1:
        return memo[i][tar]
    no = solve(i-1, num , tar , memo)
    take = 0
    if num[i] <= tar:
        take = solve(i-1 , num , tar-num[i] , memo)
    memo[i][tar] = (no + take)
    return memo[i][tar]

def findWays(num: List[int], tar: int) -> int:
    # Write your code here.
    n = len(num)
    memo = [[-1 for i in range(tar+1)] for j in range(n)]
    return  solve(n-1 , num , tar , memo)

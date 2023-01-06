"""

Given an array ‘ARR’, partition it into two subsets (possibly empty)
 such that their union is the original array.
  Let the sum of the elements of these two subsets be ‘S1’ and ‘S2’.
Given a difference ‘D’,
 count the number of partitions in which ‘S1’ is greater than or equal to ‘S2’ and the
 difference between ‘S1’ and ‘S2’ is equal to ‘D’. Since the answer may be too large, return it modulo ‘10^9 + 7’.
If ‘Pi_Sj’ denotes the Subset ‘j’ for Partition ‘i’. Then, two partitions P1 and P2 are considered different if:
1) P1_S1 != P2_S1 i.e, at least one of the elements of P1_S1 is different from P2_S2.
2) P1_S1 == P2_S2, but the indices set represented by P1_S1 is not equal to the indices
set of P2_S2. Here, the indices set of P1_S1 is formed by taking the indices of the elements
 from which the subset is formed.
Refer to the example below for clarification.

Note that the sum of the elements of an empty subset is 0.
For example :
If N = 4, D = 3, ARR = {5, 2, 5, 1}
There are only two possible partitions of this array.
Partition 1: {5, 2, 1}, {5}. The subset difference between subset sum is: (5 + 2 + 1) - (5) = 3
Partition 2: {5, 2, 1}, {5}. The subset difference between subset sum is: (5 + 2 + 1) - (5) = 3
These two partitions are different because, in the 1st partition,
 S1 contains 5 from index 0, and in the 2nd partition, S1 contains 5 from index 2.

Input Format :
The first line contains a single integer ‘T’ denoting the number of test cases, then each test case follows:

The first line of each test case contains two space-separated integers,
 ‘N’ and ‘D,’ denoting the number of elements in the array and the desired difference.

The following line contains N integers denoting the space-separated integers ‘ARR’.

Output Format :
For each test case, find the number of partitions satisfying the above conditions modulo 10^9 + 7.
Output for each test case will be printed on a separate line.

Note :
You are not required to print anything; it has already been taken care of. Just implement the function.

Constraints :
1 ≤ T ≤ 10
1 ≤ N ≤ 50
0 ≤ D ≤ 2500
0 ≤ ARR[i] ≤ 50



"""

""" memorization """
mod = 1e9+7
def  solve(i , d , arr , tar , memo):
    if i == 0:
        if tar == 0 and arr[0]==0:
            return 2
        if tar == 0 or tar == arr[0]:
            return 1
        return 0
    if memo[i][tar] != -1:
        return memo[i][tar]
    take = 0
    no = solve(i-1 , d , arr , tar , memo)
    if arr[i] <= tar:
        take = solve(i-1 , d , arr , tar-arr[i] , memo)
    memo[i][tar]  =  int((no + take) % mod)
    return memo[i][tar]


def countPartitions(n: int, d: int, arr: List[int]) -> int:
    # write your code here
    sum = 0
    for i in arr:
        sum += i
    if (sum-d) % 2 == 1:
        return 0
    if (sum-d) < 0:
        return 0
    tar = (sum - d) // 2
    memo= [[-1 for i in range(tar+1)] for j in range(n)]
    return solve(n-1 , d , arr , tar , memo)



""" Bottom - up """

def countPartitions(n: int, d: int, num: List[int]) -> int:
    # write your code here
    sum = 0
    for i in num:
        sum += i
    if (sum-d) % 2 == 1:
        return 0
    if (sum-d) < 0:
        return 0
    tar = (sum - d) // 2
    dp = [[0 for i in range(tar+1)] for j in range(n)]
    if num[0] == 0:
        dp[0][0] = 2
    else:
        dp[0][0] = 1

    if num[0] != 0 and num[0] <= tar:
        dp[0][num[0]] = 1
    for i in range(1 , n):
        for j in range(tar+1):
            no = dp[i-1][j]
            take  = 0
            if num[i] <= j:
                take =  dp[i-1][j-num[i]]
            dp[i][j] = int((take + no)%mod)
    return dp[n-1][tar]

"""

Problem Statement
Suggest Edit
There is a frog on the 1st step of an N stairs long staircase.
 The frog wants to reach the Nth stair. HEIGHT[i] is the height of the
  (i+1)th stair.If Frog jumps from ith to jth stair, the energy lost in the jump is given by
   |HEIGHT[i-1] - HEIGHT[j-1] |.In the Frog is on ith staircase, he can jump either to (i+1)th stair or
   to (i+2)th stair. Your task is to find the minimum total energy used by the frog to reach from 1st stair to Nth stair.

For Example
If the given ‘HEIGHT’ array is [10,20,30,10],
the answer 20 as the frog can jump from 1st stair to 2nd stair (|20-10| = 10 energy lost)
 and then a jump from 2nd stair to last stair (|10-20| = 10 energy lost). So, the total energy lost is 20.

Input Format:
The first line of the input contains an integer, 'T,’ denoting the number of test cases.

The first line of each test case contains a single integer,' N’, denoting the number of stairs in the staircase,

The next line contains ‘HEIGHT’ array.

Output Format:
For each test case, return an integer corresponding to the minimum energy lost to reach the last stair.

Note:
You do not need to print anything. It has already been taken care of. Just implement the given function.

Constraints:
1 <= T <= 10
1 <= N <= 100000.
1 <= HEIGHTS[i] <= 1000 .

Time limit: 1 sec

Sample Input 1:
2
4

10 20 30 10
3
10 50 10

Sample Output 1:
20
0


"""

from os import *
from sys import *
from collections import *
from math import *

from typing import *

def solve(arr , i):
    if(i==0):
        return 0
    first = solve(arr , i-1) + abs(arr[i] - arr[i-1])
    second = float("inf")
    if i > 1:
        second = solve(arr ,i-2) + abs(arr[i] - arr[i-2])
    return min(first , second)
def frogJump(n: int, heights: List[int]) -> int:

    # Write your code here.
    return solve(heights , n-1)

#top down Approach
def solve(arr , i , memo):
    if(i==0):
        return 0
    if(memo[i]  != -1):
        return memo[i]

    first = solve(arr , i-1 , memo) + abs(arr[i] - arr[i-1])
    second = float("inf")
    if i > 1:
        second = solve(arr ,i-2 , memo) + abs(arr[i] - arr[i-2])
    memo[i] = min(first , second)
    return memo[i]
def frogJump(n: int, heights: List[int]) -> int:
    memo = [-1]*n
    return solve(heights , n-1 , memo)

# bottom up
def frogJump(n: int, heights: List[int]) -> int:
    dp = [0]*n
    dp[0] = 0
    second = float("inf")
    for i in range(1 , n):
        first = dp[i-1] + abs(heights[i] - heights[i-1])
        if i > 1:
            second = dp[i-2] + abs(heights[i] - heights[i-2])
        dp[i] = min(first , second)
    return dp[n-1]

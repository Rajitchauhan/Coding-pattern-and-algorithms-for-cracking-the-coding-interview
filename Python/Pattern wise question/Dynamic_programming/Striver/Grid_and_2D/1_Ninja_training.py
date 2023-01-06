"""

Ninja is planing this ‘N’ days-long training schedule.
 Each day, he can perform any one of these three activities.
  (Running, Fighting Practice or Learning New Moves).
   Each activity has some merit points on each day.
    As Ninja has to improve all his skills,
    he can’t do the same activity in two consecutive days.
     Can you help Ninja find out the maximum merit points Ninja can earn?
You are given a 2D array of size N*3 ‘POINTS’ with the points corresponding to each day and activity.
 Your task is to calculate the maximum number of merit points that Ninja can earn.
For Example
If the given ‘POINTS’ array is [[1,2,5], [3 ,1 ,1] ,[3,3,3] ],the answer will be 11 as 5 + 3 + 3.

Input Format:
The first line of the input contains an integer, 'T,’ denoting the number of test cases.

The first line of each test case contains a single integer,' N’, denoting the number of days.

The next ‘N’ lines of each test case have 3 integers corresponding to POINTS[i].

Output Format:
For each test case, return an integer corresponding to the maximum coins  Ninja can collect.

Note:
You do not need to print anything. It has already been taken care of. Just implement the given function.

Constraints:
1 <= T <= 10
1 <= N <= 100000.
1 <= values of POINTS arrays <= 100 .



"""

from typing import *


def solve(day , points , last , memo):

    if(day==0):
        maxi = 0
        for i in range(3):
            if i != last:
                maxi = max(maxi , points[day][i])
        memo[day][last] = maxi
        return memo[day][last]
    if memo[day][last] != -1:
        return memo[day][last]


    maxi = 0
    for i in range(3):
        if i != last:
           activity =  solve(day-1 , points , i , memo) + points[day][i]
           maxi = max(maxi , activity)
    memo[day][last] = maxi
    return memo[day][last]

def ninjaTraining(n: int, points: List[List[int]]) -> int:

    # Write your code here.
   memo = [[-1 for j in range(4)] for i in range(n)]
   return solve(n-1 , points , 3 , memo)

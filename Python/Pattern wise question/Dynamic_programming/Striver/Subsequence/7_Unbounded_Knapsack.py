"""


Problem Statement
You are given ‘N’ items with certain ‘PROFIT’ and ‘WEIGHT’ and a knapsack with weight capacity ‘W’
. You need to fill the knapsack with the items in such a way that you get the maximum profit.
 You are allowed to take one item multiple times.
For Example
Let us say we have 'N' = 3 items and a knapsack of capacity 'W' =  10
'PROFIT' = { 5, 11, 13 }
'WEIGHT' = { 2, 4, 6 }

We can fill the knapsack as:

1 item of weight 6 and 1 item of weight 4.
1 item of weight 6 and 2 items of weight 2.
2 items of weight 4 and 1 item of weight 2.
5 items of weight 2.

The maximum profit will be from case 3 i.e ‘27’. Therefore maximum profit = 27.

Input Format
The first line contains a single integer ‘T’ denoting the number of test cases.

The first line of each test contains two integers ‘N’ -
number of elements in the array and ‘W’ - Capacity of the knapsack.

The second line of each test case contains profiti -
 profit of the item at the ‘i-th’ index.

The third line of each test case contains weighti -
 weight of the item at the ‘i-th’ index

Output Format
For each test case,
return an integer denoting the maximum profit that can be obtained by filling the knapsack.

Note:
You do not need to print anything;
 it has already been taken care of. Just implement the given function.

Constraints
1 <= T <= 50
1 <= N <= 10^3
1 <= W <= 10^3
1 <= PROFIT[ i ] , WEIGHT[ i ] <= 10^8

"""

""" Recursion  """
def solve(i , w , profit , weight):
    if i == 0:
        return (w//weight[0]) * profit[0]
    no = solve(i-1 , w , profit , weight)
    take = 0
    if weight[i] <=w:
        take  = solve(i , w-weight[i] , profit , weight) + profit[i]
    return max(no , take)

def unboundedKnapsack(n, w, profit, weight):
    return  solve(n-1 , w , profit , weight)

""" memorization """
def solve(i , w , profit , weight , memo):
    if i == 0:
        return (w//weight[0]) * profit[0]
    if memo[i][w] != -1:
        return memo[i][w]
    no = solve(i-1 , w , profit , weight , memo)
    take = 0
    if weight[i] <=w:
        take  = solve(i , w-weight[i] , profit , weight , memo) + profit[i]
    memo[i][w] =  max(no , take)
    return memo[i][w]

def unboundedKnapsack(n, w, profit, weight):
    memo = [[-1 for i in range(w+1)] for j in range(n)]

    return  solve(n-1 , w , profit , weight , memo)

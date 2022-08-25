"""
task :: given an unlimited supply of coin of given denominations ,
 find the total of distinct way to get desired changes

Input: S = { 1, 3, 5, 7 }, target = 8

The total number of ways is 6

{ 1, 7 }
{ 3, 5 }
{ 1, 1, 3, 3 }
{ 1, 1, 1, 5 }
{ 1, 1, 1, 1, 1, 3 }
{ 1, 1, 1, 1, 1, 1, 1, 1 }


Input: S = { 1, 2, 3 }, target = 4

The total number of ways is 4

{ 1, 3 }
{ 2, 2 }
{ 1, 1, 2 }
{ 1, 1, 1, 1 }
"""


def coin_change(coin , target):
     n = len(coin)

     T = [[0] * (target + 1) for i in range(n + 1)]

     for i in range(n + 1):
         T[i][0] = 1

     for i in range(1, n + 1):
         for j in range(1, target + 1):
             if coin[i - 1] > j:
                 T[i][j] = T[i - 1][j]
             else:
                 T[i][j] = T[i - 1][j] + T[i][j - coin[i - 1]]

     return T[n][target]

coin = [ 1, 2 , 3]
sum=5
print(coin_change(coin , sum))

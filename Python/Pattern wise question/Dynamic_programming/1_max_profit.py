"""
Task :: find out max profit.
weight :: [1 , 3 , 4 , 5]
value :: [1 , 4 , 5 ,  7]
capacity(W) :: 7 kg
"""
""" Using Recursion
def max_profit(wt , val , W,n):
    if n == 0 or W ==0:
        return 0
    if wt[n-1] <=  W:
        return max(val[n-1] + max_profit(wt , val , W-wt[n-1] , n-1) , max_profit(wt , val , W , n-1))
    elif wt[n-1] > W:
        return max_profit(wt , val , W , n-1)

#output = 220
val = [60 , 100 , 120]
wt=[10 , 20 , 30]
"""
""" Memoirazation """
def max_profit(wt , val , W,n):
    t = [[-1 for x in range(W+1)] for x in range(n+1)]
    if n == 0 or W ==0:
        return  0
    if t[n][W] != -1:
        return t[n][W]
    if wt[n-1]<=W:
        t[n][W] = max(val[n-1] + max_profit(wt , val , W-wt[n-1] , n-1) , max_profit(wt , val , W , n-1))
    else:
        return max_profit(wt , val , W , n-1)


    return t[n][W]


""" top down apporch """
def max_profit(wt , val , W,n):
    t = [[0 for x in range(W+1)]for x in range(n+1)]
    for n in range(n+1):
        for w in range(W+1):
            if n ==0 or  w==0:
                t[n][w] = 0
            elif wt[n-1] <= w:
                t[n][w] = max(val[n-1] + t[n-1][w-wt[n-1]] , t[n-1][w])
            else:
                t[n][w] = t[n-1][w]

    return t[n][w]


val = [60 , 100 , 120]
wt=[10 , 20 , 30]

n=len(wt)

W=50
print(max_profit(wt , val , W , n))

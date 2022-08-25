"""
Given a rod of length n inches and an array of prices that
contains prices of all pieces of size smaller than n.
Determine the maximum value obtainable by cutting up the rod and selling the pieces.
For example, if length of the rod is 8 and the values of different pieces are given as following,
 then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20
And if the prices are as following, then the maximum obtainable value is 24
(by cutting in eight pieces of length 1)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 3   5   8   9  10  17  17  20


#wrong
def rod_cutting(price ,target ,  n):

    # `T[i]` stores the maximum profit achieved from a rod of length `i`
     n = len(price)

     T = [[0] * (target + 1) for _ in range(n + 1)]

     for i in range(n + 1):
         T[i][0] = 1

     for i in range(1, n + 1):
         for j in range(1, target + 1):
             if price[i - 1] > j:
                 T[i][j] = T[i - 1][j]
             else:
                 T[i][j] =max(T[i - 1][j] , price[i-1] + T[i][j - (i-1)])

     return T[n][target]

"""
def rod_cutting(price , n):

    # `T[i]` stores the maximum profit achieved from a rod of length `i`
    T = [0] * (n + 1)

    # consider a rod of length `i`
    for i in range(1, n + 1):
        # divide the rod of length `i` into two rods of length `j`
        # and `i-j` each and take maximum
        for j in range(1, i + 1):
            T[i] = max(T[i], price[j - 1] + T[i - j])

    # `T[n]` stores the maximum profit achieved from a rod of length `n`
    return T[n]


price = [1, 5, 8, 9, 10, 17, 17, 20]
n=len(price)
print(rod_cutting(price , n))

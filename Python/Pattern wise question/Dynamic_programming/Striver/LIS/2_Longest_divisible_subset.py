from os import *
from sys import *
from collections import *
from math import *

from typing import List


def divisibleSet(arr: List[int]) -> List[int]:
    # Write your code here.
    arr.sort()
    n = len(arr)

    dp = [1]*n
    hash = [0]*n
    maxi = -1
    for i in range(n):
        hash[i] = i
        for j in range(i):
            if arr[i] % arr[j] == 0:
                #dp[i] = max(dp[i] , 1+dp[j])
                if dp[i] < 1 + dp[j]:
                    dp[i] = 1 + dp[j]
                    hash[i] = j
        #maxi = max(maxi , dp[i])
        if dp[i] > maxi:
            maxi = dp[i]
            last_index = i
    res = []
    res.append(arr[last_index])
    while hash[last_index] != last_index:
        last_index = hash[last_index]
        res.append(arr[last_index])
    return res[::-1]

    return maxi

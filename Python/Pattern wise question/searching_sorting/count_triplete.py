"""
Problem :: count triplete with sum smaller than x
"""

def count_triplete(arr , x):
    arr.sort()
    n = len(arr)
    ans = 0
    for i in range(0,n-2):
        j = i+1
        k = n - 2
        while j<k:
            if arr[i]+arr[j]+arr[k]>=k:
                k -= 1
            else:
                ans += k-j
                j += 1
    return ans

arr = [2,3,41,21,12,30,1,5]
x = 16
print(count_triplete(arr , x))

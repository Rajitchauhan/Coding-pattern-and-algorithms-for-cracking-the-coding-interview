#stock  buy and sell

def maxProfit(arr , n):
    profit = 0
    for i in range(1 , n):
        if arr[i]> arr[i-1]:
            profit += arr[i] - arr[i-1]
    return profit

arr = [100 , 10 , 260 , 310 , 4 , 535 , 695]
n=len(arr)
print(maxProfit(arr , n))

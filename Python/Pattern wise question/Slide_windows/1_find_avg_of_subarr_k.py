"""

Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

Output: [2.2, 2.8, 2.4, 3.6, 2.8]
"""
class Sliding:
    def avg(self , k , arr):
        i , j = 0 , 0
        sum = 0
        ans = []
        for j in range(len(arr)):
            sum += arr[j]
            if(j >= k-1):
                ans.append(sum/k)
                sum -= arr[i]
                i += 1
        return ans



if __name__ == "__main__":
    arr = [1 , 3 , 2 , 6 , -1 , 4 , 1 , 8 , 2]
    k = 5
    obj = Sliding()
    res = obj.avg(k , arr)
    for i in res:
        print(i , end=" ")

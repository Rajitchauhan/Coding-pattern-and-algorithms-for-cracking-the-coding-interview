def missingAndrepeating(arr , n):
    ans = [0]*2
    for i in range(n):
        if arr[abs(arr[i]) -1] > 0:
            arr[abs(arr[i]) -1] = - arr[abs(arr[i]) -1]
        else:
            ans[0] = abs(arr[i])

    for i in range(n):
        if  arr[i] > 0:
            ans[1] = i+1
        
    return ans

arr = [1,2,2,4]
n=len(arr)
print(missingAndrepeating(arr , n))

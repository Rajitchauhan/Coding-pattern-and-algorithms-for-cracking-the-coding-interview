"""
intialize start = 0 , end = n - 1
while start < end
swap start with end
start += 1
end -= 1
return array

"""
def reverse(arr , start , end , n):
    while(start < end):
        arr[start] , arr[end] = arr[end] , arr[start]
        start += 1
        end -= 1
    return arr

arr= [1,2,3,4,5]
#arr = "Rajit
n=len(arr)
start , end = 0 , n-1

print(reverse(arr , start , end , n))

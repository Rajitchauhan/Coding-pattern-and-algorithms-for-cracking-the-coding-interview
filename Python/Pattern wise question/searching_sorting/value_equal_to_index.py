def valueEqaulToINDEX(arr , n):
    l =[]
    for i in range(n):
        if arr[i] == i+1:
            l.append(i+1)
    return l 
arr = [1 ,2 ,3 ,5]
n=len(arr)
print(valueEqaulToINDEX(arr , n))

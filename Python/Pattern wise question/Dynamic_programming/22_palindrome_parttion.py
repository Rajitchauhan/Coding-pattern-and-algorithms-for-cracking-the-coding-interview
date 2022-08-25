import sys
def isPalin(A):
    low = 0
    high = len(A)-1
    status = True
    while(low<high):
        if A[low]==A[high]:
            low += 1
            high -= 1
        else:
            status = False
            break
    return status
            
def minCut(A , i ,j):
    t = [[-1 for x in range(j+1)]for x in range(i+1)]
   
    if i>=j:
        return 0
    if isPalin(A)==True:
        return 0
    if t[i][j] != -1:
        return t[i][j]
    mn = sys.maxsize

    for  k in range(i , j):
        tmp = 1+minCut(A , i , k) + 
        minCut(A , k+1 , j)
        mn = min(mn , tmp)
    return mn
A = 'nitik'
i=0
j=len(A)-1
print(minCut(A , i , j))
        
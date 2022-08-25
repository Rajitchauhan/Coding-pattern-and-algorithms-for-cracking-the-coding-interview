"""

X : ['a' , 'b' , 'c' , 'd' , 'g' , 'h']
Y : ['a' , 'b' , 'e' , 'd' , 'f' , 'h' , 'r']
output : abdh


"""
def printLCS(A,B  , m,  n):
    t = [[0 for i in range(n+1)] for i in range(m+1)]
    lt = []

    for i in range(m+1):
        for j in range(n+1):
            if m==0 or n==0:
                t[i][j] = 0
            elif A[i-1]==B[j-1]:
                t[i][j] = 1+  t[i-1][j-1]
            else:
                t[i][j] = max(t[i][j-1] , t[i-1][j])


    i=m
    j=n
    #lt = []
    s=""
    while(i>0 and j>0):
        if A[i-1]==B[j-1]:
            #lt.append(A[i-1])
            s += A[i-1]
            i -= 1
            j -= 1

        else:
            if t[i][j-1] > t[i-1][j]:
                j -= 1
            else:
                i -= 1

    #print(*lt[::-1])
    print(s[::-1])


A = ['a' , 'b' , 'c' , 'd' , 'g' , 'h']
B = ['a' , 'b' , 'e' , 'd' , 'f' , 'h' , 'r']

printLCS(A , B , len(A) , len(B))

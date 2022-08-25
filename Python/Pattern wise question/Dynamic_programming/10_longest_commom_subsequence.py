"""
X : ['a' , 'b' , 'c' , 'd' , 'g' , 'h']
Y : ['a' , 'b' , 'e' , 'd' , 'f' , 'h' , 'r']
output : 4 {length}


def LCS(X ,Y , m , n):
    if m ==0 or n==0:
        return 0

    if X[m-1] == Y[n-1]:
        return 1+LCS(X , Y , m-1 , n-1)
    else:
        return max(LCS(X,Y , m-1 , n) , LCS(X,Y , m , n-1))


#Memoirazation
def LCS(X,Y , m , n):
    #t = [[-1 for i in range(n+1)] for i in range(m+1)]
    t = [[-1]*(n+1) for i in range(m+1)]
    if m==0 or n==0:
        return 0

    if t[m][n] !=  -1:
        return t[m][n]
    if X[m-1]==Y[n-1]:
        t[m][n] = 1+LCS(X,Y , m-1 , n-1)
        return t[m][n]
    else:
        t[m][n] = max(LCS(X,Y , m-1 , n) , LCS(X,Y , m , n-1))
        return t[m][n]
"""

def LCS(X,Y,m,n):

    #t = [[0]*(n+1) for i in range(m+1)]
    t = [[0 for i in range(n+1)] for j in range(m+1)]
    if m==0  or n==0:
        return 0

    for i in range(m+1):
        for j in range(n+1):
            if X[i-1]==Y[j-1]:
                t[i][j] = 1+t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j] , t[i][j-1])

    return t[m][n]


X = ['a' , 'b' , 'c' , 'd' , 'g' , 'h']
Y = ['a' , 'b' , 'e' , 'd' , 'f' , 'h' , 'r']


print(LCS(X,Y,len(X),len(Y)))

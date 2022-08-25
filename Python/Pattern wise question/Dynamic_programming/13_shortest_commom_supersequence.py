"""
A : geek
B : eke

output : 5 length{geeke}

"""

def superSequence(A , B):
    m=len(A)
    n=len(B)
    l  =  LCS(A,B ,m ,n)

    return (m+n) - l

def LCS(A , B ,m , n):

    t= [[0 for i in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j] = 0
            elif A[i-1]==B[j-1]:
                t[i][j] = 1+t[i-1][j-1]
            else:
                t[i][j] = max(t[i][j-1] , t[i-1][j])

    return t[m][n]

A = ['g' , 'e' , 'e' , 'k']
B = ['e' ,'k' , 'e']
print(superSequence(A , B ))

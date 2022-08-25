"""
A : 'heap'
B : 'pea'

output : 2 {two deletion and one insertion}
#only insertion and deletion are allow.
"""
def  min_insert_del(A , B , m , n):
    l = LCS(A , B , m, n)
    m , n = len(A) , len(B)
    ins = n - l
    dele = m - l
    return ins , dele

def LCS(A ,B ,m, n):

    t = [[0 for i in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        for j  in range(n+1):
            if i==0 or j==0:
                t[i][j] = 0
            elif A[i-1]==B[j-1]:
                t[i][j] = 1+t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j] , t[i][j-1])
    return t[m][n]

A = 'heap'
B = 'pea'
print(min_insert_del(A,B , len(A) , len(B)))

"""
Task :: minimum numbr of deletion in string to make palindrom.
S : 'agbcba'
output : 1 { only one 'g' need to deletion to make palindrom }

"""
def mini_deletion(A):
    l = LPS(A)
    dele = len(A)

    return dele-l

def LPS(A):
    B = A[::-1]
    m , n = len(A) , len(B)

    t = [[0 for i in range(n+1)]for j in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j] = 0
            elif A[i-1]==B[j-1]:
                t[i][j] = 1+ t[i-1][j-1]
            else:
                t[i][j] = max(t[i][j-1] , t[i-1][j])

    return t[m][n]

A = 'agbcba'
print(mini_deletion(A))

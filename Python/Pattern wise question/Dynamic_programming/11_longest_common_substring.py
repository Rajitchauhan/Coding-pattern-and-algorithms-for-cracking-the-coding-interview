"""
task :: print longest commom substring .

A : ['a' , 'b' , 'c' , 'd' , 'e']
B : ['a' , 'b' , 'f' , 'c' , 'e']

output :: 2 {a ,b }


#Recursion
def lcstring(A , B , m , n , count):

    if m==0  or n==0:
        return count

    if (A[m-1] ==  B[n-1]):
        return  lcstring(A , B , m-1 , n-1 , count+1)
    else:
        return max(count , max(lcstring(A , B , m-1 , n , 0) , lcstring(A , B , m , n-1 , 0)))

    return count


A = ['a' , 'b' , 'c' , 'd' , 'e']
B = ['a' , 'b' , 'f' , 'c' , 'e']

print(lcstring(A , B ,len(A) , len(B) , 0))

"""


def LCString(X, Y, m, n):

    t = [[0 for k in range(n+1)] for l in range(m+1)]

    result = 0

    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                t[i][j] = 0
            elif (X[i-1] == Y[j-1]):
                t[i][j] = t[i-1][j-1] + 1
                result = max(result, t[i][j])
            else:
                t[i][j] = 0
    return result


# Driver Code
X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'
X=  ['a' , 'b' , 'c' , 'd' , 'e']
Y =  ['a' , 'b' , 'f' , 'c' , 'e']
m = len(X)
n = len(Y)

print('Length of Longest Common Substring is',
      LCString(X, Y, m, n))

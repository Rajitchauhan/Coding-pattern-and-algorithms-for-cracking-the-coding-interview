"""
task : sequence pettern matching.
A : 'axy'
B : 'adxcefy'
output : True

"""
def pettern_match(A , B , m,n):
	l = LCS(A , B , m, n)
	res = len(A)
	return (l==res)

def LCS(A , B , m , n):
	t = [[0 for i in range(n+1)]for j in range(m+1)]

	for i in range(m+1):
		for j in range(n+1):
			if i==0 or j==0:
				t[i][j]=0
			elif A[i-1]==B[j-1]:
				t[i][j] = 1+ t[i-1][j-1]
			else:
				t[i][j] = max(t[i][j-1] , t[i-1][j])

	return t[m][n]

A = 'axy'
B = 'adxcefy'
print(pettern_match(A, B , len(A), len(B)))

"""
Task : miniimum number of insertion in a string to make a palindrom
A : "aebcbda"
output :: 2 {bcz add 'e' and 'd' instring enough to make a palindrom "adebcbeda"}

"""
def min_insertion_to_make_palidrom(A):
	B = A[::-1]
	ins = len(B)
	return ins - LCS(A)

def LCS(A):
	B = A[::-1]
	m , n= len(A) , len(B)

	t= [[0 for i in range(n+1)]for i in range(m+1)]

	for i in range(m+1):
		for j in range(n+1):
			if i==0 or j==0:
				t[i][j]=0
			elif A[i-1]==B[j-1]:
				t[i][j] = 1+ t[i-1][j-1]
			else:
				t[i][j] = max(t[i-1][j] , t[i][j-1])

	return t[m][n]

A = "aebcbda"
print(min_insertion_to_make_palidrom(A))

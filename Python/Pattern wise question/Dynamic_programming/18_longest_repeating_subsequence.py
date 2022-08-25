"""
Task : longest repeating subsequence
A = "aabebcdd"
output : 3 {abd}
"""
def longest_repeat_subsequnce(A):
	B = A 
	m ,n = len(A) , len(B)
	t = [[0 for i in range(n+1)]for i in range(m+1)]

	for i in range(m+1):
		for j in range(n+1):
			if i==0 or j==0:
				t[i][j] = 0
			elif A[i-1]==B[j-1] and i!=j:
				t[i][j] = 1+ t[i-1][j-1]
			else:
				t[i][j] = max(t[i][j-1] , t[i-1][j])

	return t[m][n]

A = "aabebcdd"
print(longest_repeat_subsequnce(A))
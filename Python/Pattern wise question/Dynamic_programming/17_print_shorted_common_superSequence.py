"""
A : geek
B : eke

output : geeke

"""

def print_superSequence(A , B ,m ,n):
	t = [[0 for i in range(n+1)]for i in range(m+1)]

	for i in range(m+1):
		for j in range(n+1):
			if i==0 or j==0:
				t[i][j] = 0
			elif  A[i-1]==B[j-1]:
				t[i][j] =  1 + t[i-1][j-1]
			else:
				t[i][j] = 1 + min(t[i][j-1] , t[i-1][j])

	
	i  , j = m  , n
	s = ""

	while(i>0 and j>0):
		if A[i-1]==B[j-1]:
			s += A[i-1]
			i -= 1
			j -= 1
		else:
			if t[i-1][j]>t[i][j-1]:
				s += B[j-1]
				j  -=  1
			else:
				s += A[i-1]
				i -= 1

	while(i>0):
		s += A[i-1]
		i -= 1
	while(j>0):
		s += B[j-1]
		j -=  1
	print(s[::-1])


A = 'geek'
B = 'eke'
#print(superSequnce(A , B , len(A) , len(B)))
print(print_superSequence(A ,B , len(A) , len(B)))

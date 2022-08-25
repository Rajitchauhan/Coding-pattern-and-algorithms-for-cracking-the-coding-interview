"""
task : matrix chain multiplication.

import sys
def solve(arr , i , j):
	t = [[-1 for x in range(j+1)]for x in range(i+1)]
	if i>=j:
		return 0
	if t[i][j] != -1:
		return t[i][j]

	t[i][j] = sys.maxsize

	for x in range(i , j):
		t[i][j] = min(t[i][j] , solve(arr , i , x) + solve(arr , x+1 , j)+ arr[i-1]*arr[x]*arr[j])

	return t[i][j]

"""
import sys
def solve(arr , i , j):
	if i>= j:
		return 0
	mn = sys.maxsize

	for k in range(i , j):
		tmp = solve(arr , i , k)+solve(arr , k+1 , j)+ arr[i-1]*arr[k]*arr[j]

		mn = min(mn , tmp)
	return mn

arr = [40 , 20 , 30 , 10 , 30]
arr = [1 , 2 , 3 , 4 , 3]
i=1
j=len(arr)-1
print(solve(arr , i, j))


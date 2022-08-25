"""
Input: mat[4][4] = { {10, 20, 30, 40},
                      {15, 25, 35, 45},
                      {27, 29, 37, 48},
                      {32, 33, 39, 50}};
              x = 29
Output: Found at (2, 1)
Explanation: Element at (2,1) is 29

Input : mat[4][4] = { {10, 20, 30, 40},
                      {15, 25, 35, 45},
                      {27, 29, 37, 48},
                      {32, 33, 39, 50}};
              x = 100
Output : Element not found
Explanation: Element 100 is not found0

"""

def row_column_wise(arr , key , n):
    i = 0
    j = n-1

    while(i>=0 and i<n) and (j>=0 and j<n):

        if arr[i][j]==key:
            return i , j
        elif arr[i][j]>key:
            j = j - 1
        else:
            i = i + 1
    return -1

mat = [ [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50] ]
x = 29
x=40
n=len(mat)
print(row_column_wise(mat , x , n))

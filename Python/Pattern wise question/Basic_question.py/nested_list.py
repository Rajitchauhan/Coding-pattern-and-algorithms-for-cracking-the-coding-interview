arr = [(1, 2), (1, 3), (2, 1), (2, 4), (0, 1), (0, 3)]
arr1 = [(0, 1), (1, 2), (0, 3), (2, 4), (1, 3), (2, 1)]

print(arr)

#print(-arr)
#bad operand type for unary -: 'list'
print(arr[1])
#(1,3)
li = [i[1] for i in arr]
print(li)
#[2, 3, 1, 4, 1, 3]
li = [i[0] for i in arr]
print(li)
#[1, 1, 2, 2, 0, 0]
li1 = [-li[0] for i in arr]
print(li)
print(arr)

print("make one list only.")
for ele in arr:
    for val in ele:
        print(val , end=" ")
print()
print("Create  Neasted list ")

matrix = [[j for j in range(2)]for i in range(5)]
print(matrix)

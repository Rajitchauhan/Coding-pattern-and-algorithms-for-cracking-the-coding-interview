from collections import defaultdict
# converts from adjacency matrix to adjacency list
def convert(a):
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
                       if a[i][j]== 1:
                           adjList[i].append(j)
    return adjList

# driver code
a =[[0, 0, 1], [0, 0, 1], [1, 1, 0]] # adjacency matrix
AdjList = convert(a)
print("Adjacency List:")
# print the adjacency list
for i in AdjList:
    print(i, end ="")
    for j in AdjList[i]:
        print(" -> {}".format(j), end ="")
    print()

# This code is contributed by Muskan Kalra.

# right choice by leetcode

graph = collections.defaultdict(list)
        if not M:
            return 0
        n = len(M)
        for i in range(n):
            for j in range(i+1,n):
                if M[i][j]==1:
                    graph[i].append(j)
                    graph[j].append(i)

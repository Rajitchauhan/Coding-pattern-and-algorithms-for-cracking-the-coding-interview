""" using adjacency matrix"""

n , m = map(int , input().split())

adjmat = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    u , v = map(int , input().split())
    adjmat[u][v] = 1
    adjmat[v][u] = 1

    

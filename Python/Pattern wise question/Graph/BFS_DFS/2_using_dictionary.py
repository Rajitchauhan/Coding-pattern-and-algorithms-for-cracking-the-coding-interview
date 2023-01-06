from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edges(self , u , v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    def genrate_edges(self):

        edges = []
        for node in self.graph:
            for neighbour in self.graph[node]:
                edges.append((node , neighbour))
        return edges

G = Graph()
G.genrate_edges()

 #declaration of graph as dictionary
G.add_edges('a','c')
G.add_edges('b','c')
G.add_edges('b','e')
G.add_edges('c','d')
G.add_edges('c','e')
G.add_edges('c','a')
G.add_edges('c','b')
G.add_edges('e','b')
G.add_edges('d','c')
G.add_edges('e','c')

# Driver Function call
# to print generated graph
print(G.genrate_edges())

"""
[('a', 'c'), ('a', 'c'), ('a', 'c'), ('a', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('c', 'e'), ('c', 'a'),
 ('c', 'b'), ('c', 'd'), ('c', 'e'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('c', 'e'), ('c', 'a'), ('c', 'b'),
  ('c', 'd'), ('c', 'e'), ('b', 'c'), ('b', 'e'), ('b', 'c'), ('b', 'e'), ('b', 'c'), ('b', 'e'), ('b', 'c'),
   ('b', 'e'), ('e', 'b'), ('e', 'c'),
('e', 'b'), ('e', 'c'), ('e', 'b'), ('e', 'c'), ('e', 'b'), ('e', 'c'), ('d', 'c'), ('d', 'c'), ('d', 'c'), ('d', 'c')]

"""

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def LienThong(self):
        visited = [False] * (self.V)
        self.DFSUtil(0, visited)
        if any(i == False for i in visited):
            return False
        return True

# Ví dụ:
g1 = Graph(5)
g1.addEdge(0, 1)
g1.addEdge(1, 2)
g1.addEdge(2, 3)
g1.addEdge(3, 0)
g1.addEdge(2, 4)
g1.addEdge(4, 2)
print("Graph is Connected" if g1.LienThong() else "Graph is not Connected")

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

    def SoThanhPhan(self):
        visited = [False] * (self.V)
        count = 0
        for i in range(self.V):
            if visited[i] == False:
                self.DFSUtil(i, visited)
                count += 1
        return count

# Ví dụ:
g1 = Graph(5)
g1.addEdge(0, 1)
g1.addEdge(1, 2)
g1.addEdge(3, 4)
print("Số thành phần liên thông của đồ thị là:", g1.SoThanhPhan())

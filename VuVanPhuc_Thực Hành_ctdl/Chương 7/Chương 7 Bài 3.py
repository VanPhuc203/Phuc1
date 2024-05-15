from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.recStack = [False for _ in range(vertices)]

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited):
        visited[v] = True
        self.recStack[v] = True
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited) == True:
                    return True
            elif self.recStack[neighbour] == True:
                return True
        self.recStack[v] = False
        return False

    def ChuTrinh(self):
        visited = [False] * (self.V)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited) == True:
                    return True
        return False

# Ví dụ:
g1 = Graph(4)
g1.addEdge(0, 1)
g1.addEdge(1, 2)
g1.addEdge(2, 3)
g1.addEdge(3, 0)
print("Đồ thị có chu trình" if g1.ChuTrinh() else "Đồ thị không có chu trình")

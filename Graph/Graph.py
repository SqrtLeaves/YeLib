from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortUtil(self, v, visited, stack):

        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        stack.insert(0, v)

    def topologicalSort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        print(stack)

    def has_cycle(self):
        visited = set()

        def dfs(root, path):
            if root not in self.graph:
                return False
            visited.add(root)
            if root in path:
                path.append(root)
                return True
            path.pop()
            for c in self.graph[root]:
                if dfs(c, path):
                    return True

            return False

        for k in self.graph:
            if k in visited:
                continue
            path = []
            if dfs(k, path):
                print(path)
                return True
        return False

#
# g = Graph(6)
# g.addEdge(0, 1);
# g.addEdge(1, 2);
# g.addEdge(2, 3);
#
# print("拓扑排序结果：")
# g.topologicalSort()
# g.has_cycle()
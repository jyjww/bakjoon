import sys
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def dfs (self, node):
        result = []
        visited = set()
        def dfs_recur(n):
            if n in visited:
                return
            visited.add(n)
            result.append(n)
            
            for v in sorted(self.graph[n]):    
                dfs_recur(v)
        dfs_recur(node)    
        return result
    
    def bfs (self, node):
        result = []
        queue = deque([node])
        visited = set([node])
        
        while queue:
            a = queue.popleft()
            result.append(a)
            for v in sorted(self.graph[a]):
                if v not in visited :
                    visited.add(v)
                    queue.append(v)
        return result

input = sys.stdin.readline
M, N, V = map(int, input().split())
graph = defaultdict(list)
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
g = Graph()
g.graph = graph     
print(*g.dfs(V))
print(*g.bfs(V))
import sys
from collections import defaultdict
input = sys.stdin.readline

def topological_sort(v):
    visited[v] = 1
    for vnext in edges[v]:
        if not visited[vnext]:
            topological_sort(vnext)
    result.append(v)

N, M = map(int, input().split())
edges = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
visited = [0]*(N+1)
result = []

for v in range(1, N+1):
    if not visited[v]:
        topological_sort(v)

result.reverse()
print(*result)
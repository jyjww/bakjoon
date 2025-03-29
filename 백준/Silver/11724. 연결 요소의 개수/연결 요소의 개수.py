import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)
def dfs (v):
    visited[v] = True
    for v_next in graph[v]:
        if not visited[v_next] :
            dfs(v_next)
input = sys.stdin.readline
N, E = map(int, input().split())
graph = defaultdict(list)
visited = [False]*(N+1)
count = 0

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1):
    if not visited[i]:  
        dfs(i)
        count += 1     
print(count)
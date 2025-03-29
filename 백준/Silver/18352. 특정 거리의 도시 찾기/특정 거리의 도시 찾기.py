import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    distance[v] = 0
    while queue:
        now = queue.popleft()
        for nextN in graph[now]:
            if not visited[nextN]:
                visited[nextN] = 1
                distance[nextN] = distance[now] +1
                queue.append(nextN)

N, M, K, X = map(int, input().split())
graph = defaultdict(list)
visited = [0]*(N+1)
distance = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    
bfs(X)
result = []
for i in range(1, N+1):
    if distance[i] == K:
        result.append(i)
        
if result :
    for city in sorted(result):
        print(city)
else:
    print(-1)
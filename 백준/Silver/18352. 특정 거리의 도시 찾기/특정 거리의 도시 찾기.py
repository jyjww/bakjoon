import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 0
    while queue:
        now = queue.popleft()
        if visited[now] >= K:
            continue
        for nextN in graph[now]:
            if visited[nextN] == -1:
                visited[nextN] = visited[now] + 1
                queue.append(nextN)

N, M, K, X = map(int, input().split())
graph = defaultdict(list)
visited = [-1] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

bfs(X)
result = []
for i in range(1, N + 1):
    if visited[i] == K:
        result.append(i)

if result:
    for city in sorted(result):
        print(city)
else:
    print(-1)

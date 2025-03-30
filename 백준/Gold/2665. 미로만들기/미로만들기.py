import sys, math
from collections import deque
input = sys.stdin.readline

def bfs(graph):
    dist = [[math.inf]*N for _ in range(N)]
    dist[0][0] = 0
    pq = deque()
    pq.append((0, 0))
    
    while pq:
        y, x = pq.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if graph[ny][nx] == 1:
                    cost = 0
                else:
                    cost = 1
                if dist[ny][nx] > dist[y][x] + cost:
                    dist[ny][nx] = dist[y][x] + cost
                    if cost == 0:
                        pq.appendleft((ny, nx))
                    else:
                        pq.append((ny, nx))
    return dist[N-1][N-1]

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]

result = bfs(graph)
print(result)

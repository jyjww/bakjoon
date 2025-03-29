import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph):
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    
    while queue:
        y, x = queue.popleft()
        
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny = y + dy
            nx = x + dx
        
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append((ny, nx))
        

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

bfs(graph)
print(graph[N-1][M-1])
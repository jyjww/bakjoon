import sys
from collections import deque
input = sys.stdin.readline
    
def bfs (box):
    result = [[[0]*M for _ in range(N)] for _ in range(H)]
    
    pq = deque()
    for h in range (H):
        for y in range(N):
            for x in range(M):
                if box[h][y][x] == 1:
                    pq.append((h, y, x))
    
    while pq:
        h, y, x = pq.popleft()
        
        # 상 하 좌 우 위 아래
        for dh, dy, dx in [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)]:
            nh = h + dh
            ny = y + dy
            nx = x + dx

            if 0 <= ny < N and 0 <= nx < M and 0 <= nh < H :
                if box[nh][ny][nx] == 0 :
                    box[nh][ny][nx] = 1
                    result[nh][ny][nx] = result[h][y][x] + 1
                    pq.append((nh, ny, nx))
                if box[nh][ny][nx] == -1 :
                    continue
    return result

M, N, H = map(int, input().split())
box = []

for h in range(H):
    layer = []
    for n in range (N):
        row = list(map(int, input().split()))
        layer.append(row)
    box.append(layer)
    
max_day = 0
ans = bfs(box)
for h in range(H):
    for y in range(N):
        for x in range(M):
            if box[h][y][x] == 0 :
                print(-1)
                exit()
            max_day = max(max_day, ans[h][y][x])
print(max_day)
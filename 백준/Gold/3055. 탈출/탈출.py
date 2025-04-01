import sys
from collections import deque
input = sys.stdin.readline

def bfs(map):
    visited = [[0]*C for _ in range(R)]
    hedge_q = deque()
    water_q = deque()
    for r in range(R):
        for c in range(C):
            if map[r][c] == 'S':
                hedge_q.append((r, c))
                visited[r][c] = 1
            if map[r][c] == '*':
                water_q.append((r, c))
            if map[r][c] == 'X':
                visited[r][c] = 1
            
    while hedge_q :
        for _ in range (len(water_q)):
            wr, wc = water_q.popleft()
            for dy, dx in directions:
                ny, nx = wr + dy, wc + dx
                if 0 <= ny < R and 0 <= nx < C:
                    if map[ny][nx] == '.':
                        map[ny][nx] = '*'
                        water_q.append((ny, nx))
        for _ in range(len(hedge_q)):
            r, c = hedge_q.popleft()
            for dy, dx in directions :
                ny, nx = r+dy, c+dx
                if 0 <= ny < R and 0 <= nx < C:
                    if map[ny][nx] == 'D':
                        return visited[r][c]
                    if map[ny][nx] == '.' and not visited[ny][nx]:
                        visited[ny][nx] = visited[r][c] + 1
                        hedge_q.append((ny, nx))
    return -1

R, C = map(int, input().split())
map = [list(map(str, input().strip())) for _ in range (R)]
directions = [(1,0), (-1,0), (0,-1), (0,1)]

ans = bfs(map)
if ans == -1 :
    print('KAKTUS')
else: print(ans)
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
ice = [list(map(int, input().strip().split())) for _ in range(N)]
iceberg = [(i, j) for i in range(N) for j in range(M) if ice[i][j] > 0]

directions = [(1,0), (-1,0), (0,-1), (0,1)]

# 나랑 연결된 빙산 칸을 찾음
def dfs (y, x, visited):
    visited[y][x] = True
    for dy, dx in directions:
        ny, nx = dy+y, dx+x
        if 0 <= ny < N and 0 <= nx < M :
            if ice[ny][nx] <= 0 or visited[ny][nx]:
                continue
            dfs(ny, nx, visited) 
#시간과 방향에 따라서 녹임                
def melt():
    global iceberg
    new_iceberg = set()
    decrease = [[0]*(M) for _ in range(N)]
    
    for i, j in iceberg:
        count = 0
        for dy, dx in directions:
            ni, nj = i+dy, j+dx
            if 0 <= ni < N and 0 <= nj < M and ice[ni][nj] == 0 :
                count += 1
        decrease[i][j] = count
    
    for i, j in iceberg:
        ice[i][j] = max(0, ice[i][j] - decrease[i][j])
        if ice[i][j] > 0:
            new_iceberg.add((i, j))
    iceberg = new_iceberg
            
year = 0
while True :
    visited = [[False]*(M) for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            if ice[i][j] > 0 and not visited[i][j]:
                dfs(i, j, visited)
                count += 1
    if count == 0 :
        print(0)
        break
    if count >= 2:
        print(year)
        break 
    melt()
    year += 1
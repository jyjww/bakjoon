import sys
input = sys.stdin.readline
def dfs(y, x):
    if floor[y][x] == '|':
        floor[y][x] = 1
        for dy in [1, -1] :
            ny = y + dy
            if (ny > 0 and ny < N) and floor[ny][x] == '|':
                dfs(ny, x)
    if floor[y][x] == '-':
        floor[y][x] = 1
        for dx in [1,-1] :
            nx = x + dx
            if (nx > 0 and nx < M) and floor[y][nx] == '-':
                dfs(y, nx)


N, M = map(int, input().split())
floor = []
for _ in range(N):
    floor.append(list(input()))
count = 0

for i in range(N):
    for j in range(M):
        if floor[i][j] == '-' or floor[i][j] == '|':
            dfs(i, j)
            count += 1
            
print(count)
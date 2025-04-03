import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(y, x):
    visited[y][x] = True
    count = 1 
    for dy, dx in directions:
        ny, nx = dy+y, dx+x
        if 0 <= ny < N and 0 <= nx < N :
            if apt[ny][nx] == 1 and not visited[ny][nx]:
                count += dfs(ny, nx)
    return count
N = int(input())
apt = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0]*(N) for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

ans = []
for i in range(N):
    for j in range(N):
        if apt[i][j] == 1 and not visited[i][j]:
            ans.append(dfs(i, j))
ans.sort()
print(len(ans))
for i in ans:
    print(i)
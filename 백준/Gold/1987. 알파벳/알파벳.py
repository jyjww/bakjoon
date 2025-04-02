import sys
input = sys.stdin.readline

def bfs(r, c):
    max_count = 1
    letter.add((r, c, map[r][c]))
    
    while letter:
        r, c, path = letter.pop()
        for dy, dx in directions :
            ny, nx = dy+r, dx+c
            if 0 <= ny < R and 0 <= nx < C:
                next_char = map[ny][nx]
                if next_char not in path:
                    letter.add((ny, nx, path+map[ny][nx]))
                    max_count = max(max_count, len(path)+1)
    return max_count

R, C = map(int, input().split())
map = [list(map(str, input().strip())) for _ in range(R)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_count = 0
letter = set()

ans = bfs(0, 0)
print(ans)
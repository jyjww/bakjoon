import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(r, c):
    global max_count
    max_count = max(max_count, len(letter))
    for dy, dx in directions :
        ny, nx = dy+r, dx+c
        if 0 <= ny < R and 0 <= nx < C:
            next_char = map[ny][nx]
            if next_char not in letter :
                letter.add(next_char)
                dfs(ny, nx)
                letter.remove(next_char) 
    return max_count
                        
R, C = map(int, input().split())
map = [list(map(str, input().strip())) for _ in range(R)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_count = 0
letter = set()
letter.add(map[0][0])

ans = dfs(0, 0)
print(ans)
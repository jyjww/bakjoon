import sys, heapq
input = sys.stdin.readline
   
def func(S, Y, X):
    heap = []
    for vs, y, x in virus :
        heapq.heappush(heap, (0, vs, y, x))
    
    while heap :
        time, vs, y, x = heapq.heappop(heap)
        if time == S:
            break
        for dy, dx in direction:
            ny, nx = dy+y, dx+x
            if 0 <= ny < N and 0 <= nx < N and plate[ny][nx] == 0:
                plate[ny][nx] = vs
                heapq.heappush(heap, (time+1, vs, ny, nx))
                
    return plate[Y-1][X-1]
            
N, K = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(N)]

virus = []
for i in range(N):
    for j in range(N):
        if plate[i][j] != 0:
            virus.append((plate[i][j], i, j))
        
S, Y, X = map(int, input().split())
direction = [(1,0), (-1,0), (0,1), (0,-1)]

virus.sort()
print(func(S, Y, X))
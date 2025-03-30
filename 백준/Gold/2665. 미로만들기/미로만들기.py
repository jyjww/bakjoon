import sys, math, heapq
input = sys.stdin.readline

def dijkstra(graph):
    dist = [[math.inf]*N for _ in range(N)]
    dist[0][0] = 0
    hpq = [(0, 0, 0)]
    while hpq :
        cost, y, x = heapq.heappop(hpq)
        
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N :
                if graph[ny][nx] == 1:
                    cost_check = 0
                else:
                    cost_check = 1
                newcost = dist[y][x] + cost_check
                if dist[ny][nx] > newcost:
                    dist[ny][nx] = newcost
                    heapq.heappush(hpq, (newcost, ny, nx))
    return dist[N-1][N-1]
N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]

result = dijkstra(graph)
print(result)
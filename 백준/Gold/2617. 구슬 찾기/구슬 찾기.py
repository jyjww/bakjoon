import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[False]*(N+1) for _ in range(N+1)]

for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b :
            graph[a][b] = 0 
            
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            if graph[a][k] == True and graph[k][b] == True :
                graph[a][b] = True
result = 0
mid = (N+1) // 2            
for a in range(1, N+1):
    light = 0
    heavy = 0 
    for b in range(1, N+1):
        if graph[a][b] == True :
            light += 1
        if graph[b][a] == True :
            heavy += 1
    if heavy >= mid or light >= mid :
        result += 1

print(result) 
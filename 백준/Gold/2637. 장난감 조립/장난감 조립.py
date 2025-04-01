import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N = int(input())
M = int(input())
indegree = [0]*(N+1)
graph = defaultdict(list)
for _ in range (M):
    a, b, c = map(int, input().split())
    graph[b].append((a, c))
    indegree[a] += 1
    
queue = deque()
dp = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    if indegree[i] == 0:
        dp[i][i] =  1
        queue.append(i)
    
while queue:
    now = queue.pop()
    for (next, count) in graph[now]:
        for i in range(1, N+1):
            dp[next][i] += dp[now][i] * count
        indegree[next] -= 1
        if indegree[next] == 0 :
            queue.append(next)
for i in range(1, N+1):
    if dp[N][i] > 0:
        print(i, dp[N][i])
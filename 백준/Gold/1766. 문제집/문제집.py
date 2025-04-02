import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0]*(N+1)
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

heap = []
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []

while heap :
    node = heapq.heappop(heap)
    result.append(node)
    for next in graph[node]:
        indegree[next] -= 1
        if indegree[next] == 0 :
            heapq.heappush(heap, next)
            
print(*result)
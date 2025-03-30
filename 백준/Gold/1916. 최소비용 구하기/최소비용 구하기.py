import sys, heapq, math
from collections import defaultdict
input = sys.stdin.readline

def dijkstra(graph, start, end):
    distance = {node : math.inf for node in graph}
    distance[start] = 0
    
    pq = [(0, start)]
    
    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        
        if now == end :
            return dist
        
        for next, cost in graph[now]:
            ttlcost = dist + cost
            if ttlcost < distance.get(next, math.inf):
                distance[next] = ttlcost
                heapq.heappush(pq, (ttlcost, next))
    return -1

N = int(input())
B = int(input())
graph = defaultdict(list)
for _ in range(B):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
start, end = map(int, input().split())
result = dijkstra(graph, start, end)
print(result)
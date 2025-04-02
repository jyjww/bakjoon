import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

build_time = [0]*(N+1)
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
result = [0]*(N+1) 

for i in range(1, N+1):
    data = list(map(int, input().split()))
    build_time[i] = data[0]
    for prereq in data [1:-1]:
        graph[prereq].append(i)     
        indegree[i] += 1            
    
queue = deque()
for i in range(1, N+1):
    if indegree[i] == 0 :
        queue.append(i)
        result[i] = build_time[i]   

while queue:
    node = queue.popleft()
    
    for vnext in graph[node]:
        indegree[vnext] -= 1
        result[vnext] = max(result[vnext], result[node]+build_time[vnext])
        if indegree[vnext] == 0 :
            queue.append(vnext)

for i in range (1, N+1):          
    print(result[i])
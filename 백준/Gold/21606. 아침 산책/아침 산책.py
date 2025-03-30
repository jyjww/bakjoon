import sys 
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    cnt = 0
    for v_next in graph[v]:
        if A[v_next] == 0:
            if not visited[v_next]:
                visited[v_next] = 1
                cnt += dfs(v_next)
        else:
            cnt +=1 
    return cnt

N = int(input())
A = [0] + list(map(int, input().strip()))
graph = defaultdict(list)
visited = [0]*(N+1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
result = 0

for i in range(1, N+1):
    if A[i] == 0 :
        if not visited[i] :
            visited[i] = 1
            cnt = dfs(i)
            result += cnt * (cnt-1)
    else :
        for v_next in graph[i]:
            if A[v_next] == 1:
                result += 1
print(result)
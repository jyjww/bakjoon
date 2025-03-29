import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v):
    for v_next in graph[v]:
        if visited[v_next] == -1:
            visited[v_next] = visited[v] ^ 1 
            if not dfs(v_next):
                return False
        elif visited[v_next] == visited[v]:
            return False
    return True

K = int(input())

for _ in range (K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [-1]*(V+1)
    is_bipartite = True
    
    for _ in range (E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    for i in range(1, V+1):
        if visited[i] == -1 :
            visited[i] = 0
            if not dfs(i):
                is_bipartite = False
                break

    print("YES" if is_bipartite else "NO")
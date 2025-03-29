import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs_stack (parent, child):
    result = []
    stack = [(child, parent)]

    while stack:
        (c, p) = stack.pop()
        if p != 0 :
            result.append((c, p))
        for c_next in graph[c]:
            if c_next != p and not visited[c_next] :
                visited[c_next] = 1 
                stack.append((c_next, c))
    result.sort()
    for c, p in result:
        print(p)
        
N = int(input())
graph = defaultdict(list)
visited = [0]*(N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs_stack(0, 1)
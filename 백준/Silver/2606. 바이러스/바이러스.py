import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    global countone
    visited[v] = 1
    for v_next in comp[v]:
        if not visited[v_next]:
            dfs(v_next)
            countone +=1

N = int(input())
E = int(input())
comp = defaultdict(list)
visited = [0]*(N+1)
countone = 0

for _ in range(E):
    a, b = map(int, input().split())
    comp[a].append(b)
    comp[b].append(a)

if not visited[1]:
    dfs(1)
    
print(countone)
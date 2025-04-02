import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs (v):
    global cycle_cnt
    visited[v] = 1
    vnext = graph[v]
    if not visited[vnext] :
        dfs(vnext)
    elif not cycle[vnext]:
        now = vnext             # 사이클 추적 용도로 임시 변수 지정
        while now != v:         # 나로 다시 돌아올때 까지
            cycle_cnt += 1      # 연결노드 카운트
            now = graph[now]    # now 갱신
        cycle_cnt += 1          # 내가 나를 가르킬때 사이클 포함
    cycle[v] = 1                # 사이클 방문 처리
T = int(input())

for _ in range(T):
    n = int(input())
    data = list(map(int, input().split()))
    graph = {i+1: v for i, v in enumerate(data)}

    visited = [0]*(n+1)         # 원본 배열 방문 처리
    cycle = [0]*(n+1)           # 사이클 방문 처리
    cycle_cnt = 0               
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)

    print(n - cycle_cnt)
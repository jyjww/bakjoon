import sys 
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def path (A, graph):
    total_path = 0
    indoor = defaultdict(int)
    
    for u in graph:
        for v in graph[u]:
            if u < v:    
                if A[u] == 1 and A[v] == 1:     
                    total_path += 2
                elif A[u] == 0 and A[v] == 1:   
                    indoor[u] +=1               
                elif A[u] == 1 and A[v] == 0 :  
                    indoor[v] += 1
    
    for outside in indoor: 
        n = indoor[outside]
        total_path += n* (n-1)  
    return total_path

N = int(input())
s = input().strip()
A = [0] + list(map(int, s))
graph = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = path(A, graph)
print(result)
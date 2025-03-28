import sys
sys.setrecursionlimit(10**6)

def find(a):
    if a!= parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    rootA = find(a)         
    rootB = find(b)
    if rootA != rootB :         
        parent[rootB] = rootA  

input = sys.stdin.readline
V, E = map(int, input().split())
tree = []
for _ in range(E):
    tree.append(list(map(int, input().split())))

tree.sort(key=lambda x: x[2])   
parent = list(range(V+1))       

ans = 0
for a, b, c in tree:
    if find(a) != find(b):     
        union(a, b)            
        ans += c              
        
print(ans)
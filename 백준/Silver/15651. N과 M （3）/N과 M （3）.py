def dfs (a, list):
    if a == m:
        ar.append(list)
        return
    
    for j in range(1, n+1):
        dfs(a+1, list+[j])

n, m = map(int, input().split())
ar = []

dfs(0, [])
for ar in ar :
    print(*ar)
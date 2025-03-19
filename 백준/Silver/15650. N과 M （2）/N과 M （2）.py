def dfs (a, list):
    if a == m :
        ar.append(list)
        return
    for j in range(1, n+1):
        if list and j < list[-1]:
            continue
        if v[j] == 0:
            v[j] =1
            dfs(a+1, list+[j]) 
            v[j] =0

n, m = map(int, input().split())
ar = []
v = [0]*(n+1)

dfs (0, [])
for ar in ar :
    ans = sorted(ar)
    print(*ans)
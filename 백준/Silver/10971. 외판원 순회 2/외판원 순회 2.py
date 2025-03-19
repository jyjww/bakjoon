def tsp (start, current, cost, count):
    global mincost
    if count == n and matrix[current][start] > 0 :
        mincost = min(mincost, cost+matrix[current][start])
        return
    for next in range (n):
        if v[next]==0 and matrix[current][next] > 0 :
            v[next] =1
            tsp (start, next, cost+matrix[current][next], count+1)
            v[next] =0
            
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
v=[0]*(n)
mincost = float('inf')

v[0] = True
tsp(0, 0, 0, 1)
print(mincost)
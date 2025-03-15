a, b = map(int, input().split())
n = int(input())

lin = [0,b]
ver = [0,a]
for __ in range(n):
    x, y = map(int, input().split())
    if x == 0 :
        lin.append(y)
    if x == 1 :
        ver.append(y)
sorted_lin = sorted(lin)
sorted_ver = sorted(ver)

max_lin = max(sorted_lin[i]-sorted_lin[i-1] for i in range(1, len(sorted_lin)))
max_ver = max(sorted_ver[i]-sorted_ver[i-1] for i in range(1, len(sorted_ver)))
print(max_lin * max_ver)
from math import prod

n = int(input())
ans = []
for i in range(n):
    ans.append(n-i)
print(prod(ans))

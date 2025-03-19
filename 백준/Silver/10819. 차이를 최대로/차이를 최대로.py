def func (lst, result):
    if len(lst) == n:
        ttl = 0
        ttl = sum(abs(lst[i] - lst[i+1]) for i in range(n-1))
        result = max(result, ttl)
    for i in range(n):
        if v[i]==0:
            v[i]=1
            lst.append(m[i])
            result = func(lst, result)
            v[i]=0
            lst.pop()
    return result
        
n = int(input())
m = list(map(int, input().split()))
v = [0]*(n)

result = func ([], 0)
print(result)
import sys

def cutlan (start, end, target):
    best = 0
    while start <= end :
        mid = (start+end)//2
        ttl = 0
        for arr in a :
            if arr >= mid :
                ttl += arr // mid
        if ttl >= target:
            best = mid
            start = mid + 1
        else :
            end = mid - 1
    return best            
N, K = map(int, input().split())
a = [int(sys.stdin.readline()) for _ in range(N)]
start = 1
end = max(a)

if N == 1 : 
    if K == a[0]:
        print(1)
    else :
        result = cutlan(start, end, K)
        print(result)
else:
    result = cutlan(start, end, K)
    print(result)
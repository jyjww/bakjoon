import sys

def getmoney (start, end):
    best = 0
    while start <= end :
        mid = (start+end) // 2
        money = mid
        count = 1
        for kk in K :
            if kk > money :
                count += 1
                money = mid
            money -= kk
        if count <= M :
            best = mid
            end = mid - 1
        else:
            start = mid + 1
    return best
N, M = map(int, input().split())
K = [int(sys.stdin.readline()) for _ in range(N)]

if M == 1 :
    result = sum(K)
else :
    result = getmoney(max(K), sum(K))
print(result)
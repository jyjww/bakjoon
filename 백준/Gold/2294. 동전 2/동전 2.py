import sys, math

def dp(arr):
    dp = [0] + [math.inf for _ in range(k)]
    
    for i in range(1, k+1):
        for coin in arr :
            if i - coin >= 0 :
                dp[i] = min(dp[i], dp[i-coin]+1)
    if dp[k] == math.inf :
        return -1
    else:
        return dp[k]
n, k = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)] 

ans = dp(arr)
print(ans)
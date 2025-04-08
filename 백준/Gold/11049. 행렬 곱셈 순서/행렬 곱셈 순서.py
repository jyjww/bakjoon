import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
for _ in range (n-1):
    p.append(int(input().split()[1]))
    
dp = [[0]*n for _ in range (n)]

for c in range(2, n+1):             # 행렬 몇 개를 묶는지
    for i in range(n-c+1):          # 시작점
        j = i + c - 1               # 끝점
        dp[i][j] = float('inf')
        for k in range(i, j):       # 괄호 나누기
            # 구간 최소 연산 + 구간+1 최소 연산 + 곱셈 연산 수 (앞행*열*뒤행)
            cost = dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j+1]
            dp[i][j] = min(dp[i][j], cost)
            
print(dp[0][n-1])
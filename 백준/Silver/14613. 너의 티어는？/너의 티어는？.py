from collections import defaultdict

win, lose, draw = map(float, input().split())

N = 20
MAX_SCORE = 3499

dp = [defaultdict(float) for _ in range(N + 1)]
dp[0][2000] = 1.0

for i in range (N):
    for s in range (MAX_SCORE + 1):
        if dp[i][s] == 0 :
            continue
        if s + 50 <= MAX_SCORE :
            dp[i + 1][s + 50] += dp[i][s] * win
        dp[i + 1][s] += dp[i][s] * draw
        if s - 50 >= 0 :
            dp[i + 1][s - 50] += dp[i][s] * lose
            
tier_ranges = [
    (0, 1499),
    (1500, 1999),
    (2000, 2499),
    (2500, 2999),
    (3000, 3499),
]

for lo, hi in tier_ranges:
    prob_sum = sum(dp[20][score] for score in range(lo, hi + 1))
    print(f"{prob_sum:.8f}")

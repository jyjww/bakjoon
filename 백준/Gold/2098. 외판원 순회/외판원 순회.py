import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

INF = float('inf')
# 도시 n개에 따라 방문 여부 2**n가지로 표현 가능 (이진수)
dp = [[INF]*n for _ in range (1 << n)]
dp[1][0] = 0    # 출발: 도시 0에서 시작하고, 방문 기록은 도시 0만 방문한 상태

def tsp (visited, current):
    for visited in range((1<<n)):
        for current in range (n):
            if dp[visited][current] == INF :
                continue
            for next_city in range (n):
                if visited & (1 << next_city) : 
                    continue
                if cost[current][next_city] == 0 :
                    continue
                next_visited = visited | (1 << next_city)
                dp[next_visited][next_city] = min (
                    dp[next_visited][next_city],
                    dp[visited][current] + cost[current][next_city]
                )
    return dp[visited][current]

tsp(1, 0)

visited_all = (1<<n) - 1 
answer = INF
for city in range(n):
    if cost[city][0] == 0 :
        continue
    answer = min (answer, dp[visited_all][city] + cost[city][0])
print(answer)
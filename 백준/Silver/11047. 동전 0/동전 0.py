n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)

amt = k
count = 0
for c in coin :
    coin_count = amt // c
    count += coin_count
    amt -= coin_count * c
    
print(count)
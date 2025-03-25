import sys, heapq

input = sys.stdin.readline
n= int(input())
num = [int(input()) for __ in range(n)]
heapq.heapify(num)
ans = 0
while len(num) > 1:
    a = heapq.heappop(num)
    b = heapq.heappop(num)
    c = a + b 
    ans += c  
    heapq.heappush(num, c)
print(ans)
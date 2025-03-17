import sys
n = int(input())
count = [0] * 10001
maxx = 0
for _ in range(n):
    a = int(sys.stdin.readline()) 
    count[a] += 1 
    if a > maxx:
        maxx = a
for i in range(maxx + 1):
    for _ in range(count[i]):
        print(i)
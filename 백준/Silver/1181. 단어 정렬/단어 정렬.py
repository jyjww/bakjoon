import sys

n = int(input())
a = [sys.stdin.readline().strip() for __ in range(n)]
newa = list(set(a))
newsort = sorted(newa, key=lambda x: (len(x), x))
for i in newsort:
    print(i)
import sys

n = int(sys.stdin.readline())
a = []

for i in range(n):
    a.append(int(sys.stdin.readline()))
b = sorted(a)

print(*b, sep='\n')
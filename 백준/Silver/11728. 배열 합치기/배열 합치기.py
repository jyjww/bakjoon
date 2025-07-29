import sys
N, M = map(int, input().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

C = sorted(A + B)
print(*C)
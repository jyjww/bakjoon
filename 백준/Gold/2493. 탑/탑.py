import sys
N = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split()))
ans = [0]*N
stack =[]
for i in range (N-1, -1, -1):
    while stack and h[i] > h[stack[-1]] :
        idx = stack.pop()
        ans[idx] = i+1
    stack.append(i)
print(*ans)
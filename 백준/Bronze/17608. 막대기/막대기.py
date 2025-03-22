import sys
N = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(N)]
stack = [a[N-1]]
for i in range (N-1, -1, -1):
    if stack[-1] < a[i] :
        stack.append(a[i])
print(len(stack))
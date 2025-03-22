import sys
K = int(input())
stack = []
for _ in range (K):
    num = int(input())
    if num == 0 :
        stack.pop()
    if num > 0 :
        stack.append(num)
if not stack:
    print(0)
else:
    print(sum(stack))
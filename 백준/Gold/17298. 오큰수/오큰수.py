import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
arr=[-1]*n  
stack = []

for i in range(n) :
    while stack and nums[i] > nums[stack[-1]]:
        idx = stack.pop()
        arr[idx] = nums[i]
    stack.append(i)
print(*arr)        
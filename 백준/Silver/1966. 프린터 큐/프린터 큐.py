import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

for i in range (n):
    case1 = list(map(int, input().split()))
    case2 = list(map(int, input().split()))
    queue = deque((i, p) for i, p in enumerate(case2))
    count = 0
    while queue:
        idx, pri = queue.popleft()
        if any(pri < pri2 for _, pri2 in queue):
            queue.append((idx, pri))
        else :
            count += 1
            if idx == case1[1]:
                print(count)
                break
from collections import deque
import sys

n = int(input())
q = []

for _ in range(n):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == "push":
        q.append(cmd[1])
    elif cmd[0] == "pop":
        print(q.pop(0) if q else -1)
    elif cmd[0] == "size":
        print(len(q))
    elif cmd[0] == "empty":
        print(0 if q else 1)
    elif cmd[0] == "front":
        print(q[0] if q else -1)
    elif cmd[0] == "back":
        print(q[-1] if q else -1)
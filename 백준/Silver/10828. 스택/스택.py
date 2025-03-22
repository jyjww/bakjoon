import sys
n = int(input())
stack = []
for i in range (n):
    cmd = sys.stdin.readline().split()
    #print(cmd)
    if cmd[0] == "push":
        stack.append(cmd[1])
    elif cmd[0] == "top":
        if len(stack) > 0 :
            print(stack[-1])
        else: print(-1)
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    else :
        if len(stack) > 0 :
            print(stack.pop())
        else : print(-1)
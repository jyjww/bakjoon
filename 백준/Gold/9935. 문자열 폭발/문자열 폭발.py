import sys 

n = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()
stack = []

for ch in n : 
    stack.append(ch)
    if ''.join(stack[-len(bomb):]) == bomb :
        for _ in range (len(bomb)):
            stack.pop()
if stack :
    print(''.join(stack))
else :
    print('FRULA')
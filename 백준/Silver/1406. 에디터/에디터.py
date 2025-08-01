import sys

word = list(map(str, input()))
N = int(input())

stack = []
for w in word:
  stack.append(w)

temp = []
for i in range (N):
  cursor = list(map(str, sys.stdin.readline().split()))
  cmd = cursor[0]

  if cmd == "P":
    stack.append(cursor[1])
    
  elif cmd == "B" :
    if stack:
      stack.pop()
      
  elif cmd == "L" :
    if stack :
      p = stack.pop()
      temp.append(p)
  
  elif cmd == "D" :      
    if temp:
      p = temp.pop()
      stack.append(p)
  
  # print("temp:", temp)
for i in range(len(temp)-1, -1, -1):
  stack.append(temp[i])
print(*stack, sep="")
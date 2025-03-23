from collections import deque
a, b = map(int, input().split())
data = []
for i in range(1, a+1):
    data.append(i)
q= deque(data)
removed = []
count = 0
while q:
    count += 1
    if count % b == 0:
        popped = q.popleft()
        removed.append(popped)
    else :
        q.append(q.popleft())

print(f"<" + ", ".join(map(str, removed)) + ">")
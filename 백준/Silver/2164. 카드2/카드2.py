from collections import deque

n = int(input())
data = []
for num in range(1, n+1):
    data.append(num)
queue = deque(data)
count = 1
while queue:
    if len(queue) == 1:
        print(queue[0])
        break
    if count % 2 == 0 :
        queue.append(queue.popleft())
        count +=1
    elif count % 2 != 0 :
        queue.popleft()
        count += 1
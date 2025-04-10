import sys, heapq
input = sys.stdin.readline

n = int(input())
lect = []
for _ in range(n):
    a, b, c = map(int, input().split())
    lect.append((a, b, c))
    
lect.sort(key=lambda x : (x[1], x[2], x[0]))
# print(lect)
room = [0] * n
q = []
count = 0

for i, start, end in lect :
    if q and q[0][0] <= start:
        end_time, room_num = heapq.heappop(q)
    else :
        count += 1 
        room_num = count
    room[i-1] = room_num
    heapq.heappush(q, (end, room_num))
    
print(count)
for num in room:
    print(num)
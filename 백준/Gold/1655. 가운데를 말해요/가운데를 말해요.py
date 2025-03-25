import heapq, sys

input = sys.stdin.readline
n=int(input())
max_heap = []
min_heap = []

for i in range(n):
    num = int(input())
    
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)
    else: 
        heapq.heappush(min_heap, num)

    if min_heap and -max_heap[0] > min_heap[0]:
        max_val = -heapq.heappop(max_heap)
        min_val = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -min_val)
        heapq.heappush(min_heap, max_val)  
    print(-max_heap[0])
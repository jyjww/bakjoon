import sys
def heappush(heap, data):
    heap.append(data)
    current = len(heap)-1
    while current > 0 :
        parent = (current-1)//2
        if heap[parent] < heap[current]:
            heap[parent], heap[current] = heap[current], heap[parent]
            current = parent
        else:
            break
def heappop(heap):
    if not heap:
        return 0
    elif len(heap) == 1:
        return heap.pop()
    pop_data, heap[0] = heap[0], heap.pop()
    current, child = 0, 1
    while child < len(heap):
        sibling = child + 1
        if sibling < len(heap) and heap[child] < heap[sibling]: 
            child = sibling
        if heap[current] < heap[child]:
            heap[current], heap[child] = heap[child], heap[current]
            current = child
            child = current * 2 + 1
        else:
            break 
    return pop_data

input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    n = int(input())
    if n > 0 :
        heappush(heap, n)
    else : 
        ans = heappop(heap)
        print(ans)
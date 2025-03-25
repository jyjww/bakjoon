import sys, heapq

input = sys.stdin.readline
n = int(input())
heap = list(map(int, input().split()))
heapq.heapify(heap)
for i in range(n-1):
    arr = list(map(int, input().split()))
    for j in range(len(arr)):
        if arr[j] > heap[0]:
            removed = heapq.heapreplace(heap, arr[j])
print(heap[0])
        
import sys
def find_height(left, right, target):
    best = 0
    while left <= right :
        mid = (left + right) // 2
        total = 0
        for tree in h :
            if tree > mid :
                total += tree - mid
        if total >= target :
            best = mid
            left = mid + 1 
        else : 
            right = mid - 1
    return best

N, M = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))
left = 0
right = max(h)
result = find_height(left, right, M)
print(result)
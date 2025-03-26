import sys

def binary(target):
    low = max(a)
    hi = sum(a)
    answer = hi
    while low <= hi:
        mid = (low + hi)// 2
        needed = countdvd(mid) 
        if needed <= target : 
            answer = mid
            hi = mid - 1
        else :
            low = mid + 1
    return answer

def countdvd (mid):
    count = 1  
    ttl = 0
    for time in a :
        if ttl + time > mid:  
            count += 1  
            ttl = time  
        else :
            ttl += time  
    return count

input = sys.stdin.readline
n, b = map(int, input().split())
a = list(map(int, input().split()))
result = binary(b)
print(result)
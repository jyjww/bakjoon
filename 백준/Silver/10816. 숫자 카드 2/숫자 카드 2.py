import sys

def findcard_low (start, end, target):
    while start < end :
        mid = (start + end)//2
        if num[mid] < target :
            start = mid + 1
        else : 
            end = mid
    return start

def findcard_up (start, end, target):
    while start < end :
        mid = (start + end)//2
        if num[mid] <= target :
            start = mid + 1
        else : 
            end = mid
    return start

input = sys.stdin.readline
N = int(input())
num = sorted(list(map(int, input().split())))
M = int(input())
Mmm = list(map(int, input().split()))

start = 0
end = len(num)
carddeck = []

for i in range(len(Mmm)) :
    target = Mmm[i]
    result = findcard_up(start, end, target)
    result2 = findcard_low(start, end, target)
    ans = result - result2
    carddeck.append(ans)
print(*carddeck)
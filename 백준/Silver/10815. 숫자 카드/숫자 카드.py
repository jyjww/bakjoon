import sys

input = sys.stdin.readline

def upper (start, end, target) :
    while start < end :
        mid = (start+end)//2
        if num[mid] <= target :
            start = mid + 1
        else :
            end = mid 
    return start
def lower (start, end, target):
    while start < end :
        mid = (start+end)//2
        if num[mid] < target :
            start = mid + 1 
        else :
            end = mid
    return start        
N = int(input())
num = sorted(list(map(int, input().split())))
M = int(input())
mmm = list(map(int, input().split()))
ans =[]
start = 0
end = N

for i in range(M):
    target = mmm[i]
    result = upper (start, end, target)
    result2 = lower (start, end, target)
    answer = result - result2
    ans.append(answer)
print(*ans)
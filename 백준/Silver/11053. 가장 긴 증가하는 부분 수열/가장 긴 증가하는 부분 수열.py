def numbers (target, data):
    start = 0
    end = len(data)-1
    
    while start <= end :
        mid = (start+end)//2
        if data[mid] >= target :
            end = mid -1
        else :
            start = mid + 1
    return start
n = int(input())
A = list(map(int, input().split()))
data = [A[0]]

for i in range (1, n):
    target = A[i]
    if data[-1] < target :
        data.append(target)
    else:
        idx = numbers(target, data)
        data[idx] = target
print(len(data))
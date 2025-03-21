def salt (start, end):
    best = float('inf')
    answer = (0, 0)
    while start < end:
        sum = A[start] + A[end]
        if abs(sum) < abs(best):
            best = sum
            answer = (A[start], A[end])
        if sum < 0 :
            start += 1
        else :
            end -= 1
    return answer
                
N = int(input())
A = sorted(list(map(int, input().split())))

start = 0
end = len(A)-1
result = salt(start, end)
if len(A) == 2:
    print(f"{A[0]} {A[1]}")
else : print(*result)
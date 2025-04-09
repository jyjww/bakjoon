import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    case = int(input())
    result = []
    for _ in range(case):
        a, b = map(int, input().split())
        result.append((a, b))
        
    result.sort(key=lambda x : (x[0], x[1]))
    
    count = 0
    yes = float('inf')
    for test, interview in result :
        if interview <= yes :
            count += 1
            yes = interview
    print(count)
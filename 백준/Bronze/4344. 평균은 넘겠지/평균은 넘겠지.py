a = int(input())

for __ in range(a):
    result = list(map(int, input().split()))
    
    avg = sum(result[1:]) / result[0]
    count = sum(1 for x in result[1:] if x > avg)
    print(f"{count/sum(result[:1])*100:.3f}%")
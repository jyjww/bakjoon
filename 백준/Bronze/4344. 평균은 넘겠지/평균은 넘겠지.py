a = int(input())

for __ in range(a):
    result = input().split()

    total = 0
    for i in range(1,len(result)):
        total += int(result[i])

    average = total / int(result[0])
    count=0
    for i in range(1, len(result)):
        if average < int(result[i]):
            count += 1
    answer = count / int(result[0])
    print(f'{answer*100:.3f}%')
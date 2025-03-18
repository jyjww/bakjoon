a = [int(input()) for __ in range(9)]
a.sort()

for i in range(len(a)):
    for j in range (i+1, len(a)):
        if sum(a) - a[i] - a[j] == 100:
            for k in range (len(a)):
                if k == i or k == j:
                    continue
                else:
                    print(a[k])
            exit()
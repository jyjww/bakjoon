n = int(input())
a = [int(input()) for __ in range (n)]
b = [1, 2, 4]
count = 0
for a in a:
    if a <= 3 :
        print(b[a-1])
    if a > 3 : 
        for j in range (3, 12):
            num = b[j-1] + b[j-2] + b[j-3]
            b.append(num)
        print(b[a-1])
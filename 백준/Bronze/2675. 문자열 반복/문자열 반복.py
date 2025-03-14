a = int(input())
for __ in range(a):
    result = input().split()
    result2 = result[1]
    for i in range(len(result2)):
        b = (result2[i]*int(result[0]))
        if i < len(result2) -1 :
            print(b, end="")
        else:
            print(b)
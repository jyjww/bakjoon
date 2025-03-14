total=1
for __ in range(3):
    result = sum(list(map(int,input().split())))
    total *= result
list = list(map(int,str(total)))
for i in range(10):
    data = list.count(i)
    print(data)
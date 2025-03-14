A, B, V = map(int, input().split())
a = (V-A)/(A-B)
if a == int(a):
    print(int(a)+1)
else :
    print(int(a)+2)
#에라토스테네스의 체
prime = [True]*10001
prime[0:2]=[False, False]
for i in range (2, 10001):
    for j in range (i+i, 10001, i):
        prime[j]=False

a = int(input())
for __ in range(a):
    b=int(input())
    for i in range(b//2, 10000):
        if prime[b-i] and prime[i]:
            print(b-i, i)
            break
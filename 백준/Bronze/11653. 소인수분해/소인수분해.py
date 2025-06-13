num = int(input())

def prime(num):
    i = 2
    factors = []
    while i * i <= num :
        while num % i == 0:
            factors.append(i)
            num //= i
        i += 1
    if num > 1:
        factors.append(num)
    return factors

result = prime(num)
for a in result:
    print(a)
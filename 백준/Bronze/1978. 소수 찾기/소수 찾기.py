a = int(input())
b = list(map(int, input().split()))

count = 0
for num in b:
    if num < 2:
        continue

    is_prime = True
    for c in range(2, num):
        if num % c == 0:
            is_prime = False
            break

    if is_prime:
        count += 1

print(count)

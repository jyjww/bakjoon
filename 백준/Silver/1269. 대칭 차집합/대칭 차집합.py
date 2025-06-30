x, y = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

result = A.symmetric_difference(B)

print(len(result))

N, K = map(int, input().split())
item = []
for _ in range(N):
    w, v = map(int, input().split())
    item.append((w, v))

bag = [0]*(K+1)
for w, v in item:
    for j in range(K, w-1, -1):
        bag[j] = max(bag[j], bag[j-w]+v)

print(max(bag))
import sys

def gongugi(left, right, target):
    best = 0
    while left <= right :
        mid = (left + right) // 2
        count = 1
        last_install = h[0]
        for home in h :
            if home - last_install >= mid :
                count += 1 
                last_install = home
        if count >= target :
            best = mid
            left = mid + 1 
        else :
            right = mid - 1
    return best

N, C = map(int, sys.stdin.readline().split())
hh = [int(sys.stdin.readline()) for _ in range(N)]
h = sorted(hh)
left = 0
right = max(h)
result = gongugi(left, right, C)
print(result)
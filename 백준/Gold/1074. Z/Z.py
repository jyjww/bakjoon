n, r, c = map(int, input().split())

x = 0
y = 0
goal = 0
# c 열 r 행

def z (n, r, c, goal):
    if n == 0 :
        return goal
    
    while n > 0:
        half = 2**(n-1)
        size = half * half
        if ( r < half and c < half ) :# 1분면
            pass
        elif ( r < half and c >= half ) :# 2분면
            goal += size
            c -= half
        elif ( r >= half and c < half ) : # 3분면
            goal += 2*size
            r -= half
        else :  # 4분면
            goal += 3*size
            r -= half
            c -= half
        n -=1
    return n, r, c, goal

ans = z (n, r, c, goal)

print(ans[3])
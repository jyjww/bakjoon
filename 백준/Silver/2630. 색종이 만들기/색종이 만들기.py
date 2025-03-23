def cutpaper (x, y, size):
    global count_w, count_b
    if same_color (x, y, size) :
        if paper[y][x] == 0 :
            count_w += 1
        else: 
            count_b += 1
        return 
    half = size // 2   
    cutpaper(x, y, half) 
    cutpaper(x+half, y, half)    
    cutpaper(x, y+half, half)    
    cutpaper(x+half, y+half, half)

def same_color (x, y, size):
    color = paper[y][x]
    for j in range (y, y+size):
        for i in range (x, x+size):
            if paper[j][i] != color :
                return False
    return True
N = int(input())
paper = [list(map(int, input().split())) for _ in range (N)]
x = 0
y = 0
size = N
count_w = 0
count_b = 0
cutpaper(x, y, size)
print(count_w)
print(count_b)
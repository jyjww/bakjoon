a = int(input())
b = [input() for __ in range(a)]

for i in range (a):
    total_score = 0
    current_score = 0
    for char in str(b[i]) :
        if char == "O":
            current_score += 1
            total_score += current_score
        else :
            current_score = 0
    print(total_score)
from itertools import combinations

a = [int(input()) for __ in range(9)]
a.sort()
for comb in combinations(a, 7):
    if sum(comb) == 100:
        c = list(comb)
        
for c in c :
    print (c)
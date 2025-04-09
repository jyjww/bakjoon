n = input()

pt = n.split('-')

pt2 = sum(map(int, pt[0].split('+')))
for part in pt[1:]:
    pt2 -= sum(map(int, part.split('+')))
print(pt2)
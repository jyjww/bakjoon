a = input()
num = input()
parse = [n for n in str(num)]

result = []
temp = ''

for p in parse :
    if p.isdigit():
        temp += p
    else :
        if temp:
            result.append(temp)
            temp = ''
        result.append(temp)

if temp:
    result.append(temp)

cnt = 0    
for a in result :
    if a == '':
        continue
    cnt += int(a)
print(cnt)
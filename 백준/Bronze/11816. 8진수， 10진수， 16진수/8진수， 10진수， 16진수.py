num = input()
digits = [d for d in num]
hex = {
    "a":10,
    "b":11,
    "c":12,
    "d":13,
    "e":14,
    "f":15
}

# 10 진수
if (digits[0] != '0'):
    print (num)
else : 
# 16 진수
    if (digits[1] == 'x'):
        cnt = 0
        j = 0
        for i in range(len(digits)-1, 1, -1):
            ch = digits[i]
            if ch in hex :
                cnt += hex[ch] * (16**j)
            else:
                cnt += int(ch) * (16**j)
            j += 1
        print(cnt)
    else: 
        # 8진수
        cnt = 0
        j = 0
        for i in range(len(digits)-1, 0, -1):
            cnt += int(digits[i]) * (8**j)
            j += 1
        print(cnt)
cnt = int(input())
num = input()
digits = [int(d) for d in str(num)]

result = 0
for a in digits:
    result += a
    
print(result)
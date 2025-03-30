import sys, operator
input = sys.stdin.readline

def dfs(index, current):
    global maxV, minV
    if index == N :
        maxV = max(maxV, current)
        minV = min(minV, current)
        return 
    for i in range(4):
        if ops[i] > 0 :
            ops[i] -= 1
            nextV = op_func[i](current, num[index])
            dfs(index+1, nextV)
            ops[i] += 1

N = int(input())
num = list(map(int, input().split()))
ops = list(map(int, input().split()))
op_func = [operator.add, operator.sub, operator.mul, lambda x, y: -(-x // y) if x < 0 else x // y]

maxV = -float('inf')
minV = float('inf')

dfs(1, num[0])
print(maxV)
print(minV)
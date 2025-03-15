import sys

def bubble_sort(num):
    n = len(num)
    for i in range(n-1):
        for j in range(n - 1, i, -1):
            if num[j - 1] > num[j]:
                num[j - 1], num[j] = num[j], num[j - 1]


num = int(input())
x = list(map(int, sys.stdin.read().splitlines())) 

bubble_sort(x)
for num in x :
    print(num)
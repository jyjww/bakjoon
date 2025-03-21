import sys

def binary_search(start, end, target):
    if start > end :
        return False
    mid = (start+end) //2
    if listN[mid] == target :
        return True
    elif listN[mid] > target :
        return binary_search (start, mid-1, target)
    else: 
        return binary_search (mid+1, end, target)

N = int(sys.stdin.readline())
listN = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
listM = list(map(int, sys.stdin.readline().split()))

for target in listM:
    print(1 if binary_search(0, len(listN)-1, target) else 0)
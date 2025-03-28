import sys

def preorder(node):
    if node == '.' or node not in tree :
        return
    print(node, end='')
    left, right = tree[node]
    preorder(left)
    preorder(right)
    
def inorder (node):
    if node == '.' or node not in tree :
        return
    left, right = tree[node]
    inorder(left)
    print(node, end='')
    inorder(right)

def postorder(node):
    if node == '.' or node not in tree :
        return
    left, right = tree[node]
    postorder(left)
    postorder(right)
    print(node, end='')

input = sys.stdin.readline
N = int(input())
inputs = [sys.stdin.readline().strip() for _ in range(N)]
tree = {}

for line in inputs:
    parent, left, right = line.split()
    tree[parent] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')
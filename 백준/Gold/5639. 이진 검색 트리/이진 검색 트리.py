import sys
sys.setrecursionlimit(10**6)
class Node :
    def __init__(self, val):
        self.val = val      
        self.left = None    
        self.right = None  

def makeTree (num):
    def make(minV, maxV):
        nonlocal idx        
        if idx >= len(num):
            return None
        val = num[idx]
        if val < minV or val > maxV:
            return None
        idx += 1
        node = Node(val)
        node.left = make(minV, val)
        node.right = make(val, maxV)
        return node
    idx = 0
    return make(float('-inf'), float('inf'))

def postorder(node):
    if not node:
        return None             
    postorder(node.left)        
    postorder(node.right)       
    print(node.val, end='\n')   
    
num = []
for line in sys.stdin:
    if line.strip() == "":
        continue
    num.append(int(line.strip()))
    
tree = makeTree(num)
postorder(tree)
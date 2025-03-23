class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyQueue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self.count = 0
        
    def empty(self):
        return 1 if self.front_node is None else 0

    def size(self):
        return self.count
    
    def push(self, data):
        new_node = Node(data)
        if self.rear_node is None :
            self.rear_node = self.front_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node
        self.count += 1 
    
    def pop(self):
        if self.front_node is None :
            return -1
        node = self.front_node
        self.front_node = self.front_node.next
        if self.front_node is None:
            self.rear_node = None
        self.count -= 1
        return node.data
    
    def front(self):
        if self.front_node is None:
            return -1
        return self.front_node.data
    
    def back (self):
        if self.rear_node is None:
            return -1
        return self.rear_node.data

import sys

if __name__ == "__main__" :
    q = MyQueue()
    
    n = int(input())
    for i in range(n):
        cmd = sys.stdin.readline().split()
        if cmd[0] == "push":
            q.push(cmd[1])
        elif cmd[0] == "pop":
            print(q.pop())
        elif cmd[0] == "front":
            print(q.front())
        elif cmd[0] == "back":
            print(q.back())
        elif cmd[0] == "empty":
            print(q.empty())
        elif cmd[0] == "size":           
            print(q.size())
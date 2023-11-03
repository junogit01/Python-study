class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

import sys
n = int(sys.stdin.readline())

tree = {}

for _ in range(n):
    node, left, right = sys.stdin.readline().split()
    tree[node] = Node(item=node, left=left, right=right)

# 8
# A B C
# B D E
# C F G
# D H .
# E . .
# F . .
# G . .
# H . .

# 전위순회 : 루트 -> 왼쪽 -> 오른쪽
def preorder(node):
    print(node.item, end=" ")
    if node.left != ".":
        preorder(tree[node.left])
    if node.right != ".":
        preorder(tree[node.right])

preorder(tree["A"])
print()

# 중위순회 : 왼쪽 -> 루트 -> 오른쪽
def inorder(node):
    if node.left != ".":
        inorder(tree[node.left])
    print(node.item, end=" ")
    if node.right != ".":
        inorder(tree[node.right])
        
inorder(tree["A"])
print()

# 후위순회 : 왼쪽 -> 오른쪽 -> 루트
def postorder(node):
    if node.left != ".":
        postorder(tree[node.left])
    if node.right != ".":
        postorder(tree[node.right])
    print(node.item, end=" ")
    
postorder(tree["A"])
print()
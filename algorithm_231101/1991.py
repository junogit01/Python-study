import sys
n = int(sys.stdin.readline())

class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

tree = {}

for _ in range(n):
    node, left, right = sys.stdin.readline().split()
    tree[node] = Node(item=node, left=left, right=right)

# 전위순회 : 루트 -> 왼쪽 -> 오른쪽
def preorder(node):
    print(node.item, end="")
    if node.left != ".":
        preorder(tree[node.left])
    if node.right != ".":
        preorder(tree[node.right])
# 중위순회 : 왼쪽 -> 루트 -> 오른쪽
def inorder(node):
    if node.left != ".":
        inorder(tree[node.left])
    print(node.item, end="")
    if node.right != ".":
        inorder(tree[node.right])
# 후위순회 : 왼쪽 -> 오른쪽 -> 루트
def postorder(node):
    if node.left != ".":
        postorder(tree[node.left])
    if node.right != ".":
        postorder(tree[node.right])
    print(node.item, end="")
    
def print_orders(node):
    preorder(node)
    print()
    inorder(node)
    print()
    postorder(node)
    
print_orders(tree["A"])
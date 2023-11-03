class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:    
    def __init__(self, data):
        self.head = Node(data)
    
    def append(self, data):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)
    
    def get_node(self, index):
        current = self.head
        count = 0
        while count < index:
            current = current.next
            count += 1
        return current
    
    def delete(self, index):
        if index == 0:
            del_data = self.head.data
            self.head = self.head.next
            return del_data
        node = self.get_node(index - 1)
        del_data = node.next.data
        node.next = node.next.next
        return del_data

# 여기서부터 작성시작
# n = int(input())
# k = int(input())

# n, k = [int(i) for i in input().split()]

import sys
# n = int(sys.stdin.readline())
# k = int(sys.stdin.readline())

n, k = [int(i) for i in sys.stdin.readline().split()]

circle = LinkedList(1)

for i in range(2, n + 1):
    circle.append(i)
    
# current = circle.head
# while current is not None:
#     print(current.data)
#     current = current.next

josephus = []

index = k - 1
while n > 0:
    index = index % n
    josephus.append(circle.delete(index))
    index += k - 1
    n -= 1

print("<" + ", ".join(map(str, josephus)) + ">")

# result = "<"
# for i in josephus:
#     result += str(i) + ", "
#     if i == josephus[-1]:
#         result = result[:-2] + ">"
# print(result)

#  1  2 [ 3 ] 4  5  6  7
# (0)(1)[(2)](3)(4)(5)(6)

#  1  2  4  5 [ 6 ] 7
# (0)(1)(2)(3)[(4)](5)

#  1 [ 2 ] 4  5  7 
# (0)[(1)](2)(3)(4)

#  1  4  5 [ 7 ]
# (0)(1)(2)[(3)]

#  1  4 [ 5 ]
# (0)(1)[(2)]

# [ 1 ] 4 
# [(0)](1)

# [ 4 ]
# [(0)]
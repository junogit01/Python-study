from linked_list import LinkedList

my_ll = LinkedList("가")

my_ll.append("나")
my_ll.append("다")
my_ll.append("라")

print(my_ll.head) # <linked_list.Node object at 0x00000219B7DE40D0>
print(my_ll.head.data) # 가
print(my_ll.head.next) # <linked_list.Node object at 0x00000219B7DE4110>
print(my_ll.head.next.data) # 나
print(my_ll.head.next.next) # <linked_list.Node object at 0x00000219B7DE4190>
print(my_ll.head.next.next.data) # 다

print(f"{my_ll.delete(1)} 삭제") # "나" 삭제

print(my_ll.head) # <linked_list.Node object at 0x00000219B7DE40D0>
print(my_ll.head.data) # 가
print(my_ll.head.next) # <linked_list.Node object at 0x00000219B7DE4190>
print(my_ll.head.next.data) # 다
print(my_ll.head.next.next) # <linked_list.Node object at 0x00000219B7DE4150>
print(my_ll.head.next.next.data) # 라
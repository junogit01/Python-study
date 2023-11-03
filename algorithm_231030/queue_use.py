from queue import Queue

my_q = Queue(1)

my_q.enqueue(2)
my_q.enqueue(3)

print(my_q.head.data)
print(my_q.tail.data)
print(my_q.head.next.data)
print(my_q.head.next.next.data)

print(my_q.dequeue())
print(my_q.dequeue())
print(my_q.dequeue())
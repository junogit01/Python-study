from stack import Stack

my_stack = Stack()

print(my_stack.is_empty()) # True

my_stack.push('네이버')
my_stack.push('네이버 웹툰')
my_stack.push('마루는 강쥐 1화')
my_stack.push('마루는 강쥐 2화')

print(my_stack.is_empty()) # False

print(my_stack.pop()) # 마루는 강쥐 2화
print(my_stack.pop()) # 마루는 강쥐 1화
print(my_stack.peek()) # 네이버 웹툰
print(my_stack.peek()) # 네이버 웹툰
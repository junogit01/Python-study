# 값을 생성해서 담고 있는 a
a = [n for n in range(1000000)]
# 생성 조건만 가지고 있는 b
b = range(1000000)

# 마치 0부터 999,999까지 리스트가 동일하게 들어있는 것처럼 보이나,
print(len(a)== len(b))

import sys

# 메모리 점유는 b가 훨씬 작다.
print(sys.getsizeof(a))
print(sys.getsizeof(b)) # 100만이 아니라 100조여도 메모리 점유는 같다
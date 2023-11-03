a = [1,2,3]
b = a
c = a.copy()

# 모두 겉모습은 같다
print(a, b, c)
print(a==b)
print(b==c)

# a와 b는 같은 메모리 주소를 참조하고 있지만
# c는 완전히 다른 객체로 복사되어 있다.
# 따라서 메모리 주소가 다르다.
print(id(a), id(b) ,id(c))

# is는 메모리 주소를 비교한다.
print(a is b)
print(b is c)
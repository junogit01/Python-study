print(f"object가 가진 속성들: {dir(object)}")

class Book:
    pass

print(f"사용자 정의 클래스가 가진 속성들: {dir(Book)}")

print(f"사용자 정의 클래스만이 가진 속성들: {set(dir(Book)) - set(dir(object))}")
# print(f"사용자 정의 클래스만이 가진 속성들: {set(dir(Book)).difference(set(dir(object)))}")

# 사용자 정의 클래스가 object의 모든 속성을 정말 가지고 있을까?
common_dir = set(dir(Book)).intersection(set(dir(object)))
object_dir = set(dir(object))
print(common_dir == object_dir)
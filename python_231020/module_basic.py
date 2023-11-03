import math

print(math)
print(type(math))

print(math.pi) # math 모듈에 있는 PI라는 변수 출력
print(math.sqrt(9)) # math 모듈에 있는 sqrt라는 제곱근 구하는 함수 호출

# 파이 * r * r
# 절대 모듈 내 값을 변경해선 안된다. XXX math.pi = 3.14 XXX

print(f"반지름 5인 원의 넓이 = {5 * 5 * math.pi}")

area = 78.53981633974483
print(f"반지름 = {math.sqrt(area / math.pi)}")
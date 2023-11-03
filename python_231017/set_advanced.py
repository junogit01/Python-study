s_num1 = set([1, 2, 3, 4, 5, 6])
s_num2 = set([4, 5, 6, 7, 8, 9])

# 합집합 구하는 방법 3가지
# 1) 세트1 | 세트2 -> 세트1과 세트2의 합집합 반환
print(f"합집합 : {s_num1 | s_num2}")
# 2) 세트1.union(세트2) -> 세트1과 세트2의 합집합 반환
print(f"합집합 : {s_num1.union(s_num2)}")
# 3) 세트1.update(세트2)  -> 세트1과 세트2의 합집합 결과를 세트1에 업데이트
s_num1.update(s_num2)



s_num1 = set([1, 2, 3, 4, 5, 6])
s_num2 = set([4, 5, 6, 7, 8, 9])

# 교집합 구하는 방법 3가지
# 1) 세트1 & 세트2 -> 세트1과 세트2의 교집합 반환
print(f"교집합 : {s_num1 & s_num2}")
# 2) 세트1.intersection(세트2) -> 세트1과 세트2의 교집합 반환 
print(f"교집합 : {s_num1.intersection(s_num2)}")
# 3) 세트1.intersection_update(세트2) -> 세트1과 세트2의 교집합 결과를 세트1에 업데이트
s_num1.intersection_update(s_num2)



s_num1 = set([1, 2, 3, 4, 5, 6])
s_num2 = set([4, 5, 6, 7, 8, 9])

# 차집합 구하는 방법 3가지
# 1) 세트1 - 세트2 -> 세트1과 세트2의 차집합 반환
print(f"차집합 : {s_num1 - s_num2}")
# 2) 세트1.difference(세트2) -> 세트1과 세트2의 차집합 반환
print(f"차집합 : {s_num1.difference(s_num2)}")
# 3) 세트1.difference_update(세트2) -> 세트1과 세트2의 차집합 결과를 세트1에 업데이트
s_num1.difference_update(s_num2)



s_num1 = set([1, 2, 3, 4, 5, 6])
s_num2 = set([4, 5, 6, 7, 8, 9])

# 대칭차 구하는 방법 3가지
# 1) 세트1 ^ 세트2 -> 세트1과 세트2의 대칭차 반환
print(f"대칭차 : {s_num1 ^ s_num2}")
# 2) 세트1.symmetric_difference(세트2) -> 세트1과 세트2의 대칭차 반환
print(f"대칭차 : {s_num1.symmetric_difference(s_num2)}")
# 3) 세트1.symmetric_difference_update(세트2) -> 세트1과 세트2의 대칭차 결과를 세트1에 업데이트
s_num1.symmetric_difference_update(s_num2)
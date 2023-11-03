# 세트의 함수
s_app = set()

# 세트.add(요소) -> 세트에 새로운 요소를 추가 (이미 존재하는 요소는 넣지 않음)
s_app.add("kakaoTalk")
s_app.add("LINE")
s_app.add("kakaoTalk")

# 세트.updates(세트2) -> 세트에 다른 세트를 추가 (이미 존재하는 요소는 넣지 않음)
s_app.update(set(["kakaoTalk", "toss", "Netfilx", "Youtube", "Disney+"]))
print(s_app)

# 세트.pop() -> 임의의 요소를 꺼내기
popped_item = s_app.pop()
print(s_app, popped_item)

# 세트.remove(요소) -> 세트 내의 특정 요소를 제거 (없는 경우 KeyError)
s_app.remove("Youtube")
print(s_app)

# 세트.discard(요소) -> 세트 내의 특정 요소를 제거 (없는 경우, 변경 없음) 
s_app.discard("toss")
print(s_app)

# copy
s_app1 =s_app.copy()
print(s_app)
print(s_app1)

# 세트.clear() -> 세트의 모든 요소를 제거한다.
s_app1.clear()
print(s_app1)

# 세트.isdisjoint(세트2) -> 세트2와의 교집합 존재 여부 반환 (존재 시 false)
s1 = set({1, 2, 3, 4, 5})
s2 = set({4, 5, 6, 7})
print(s1.isdisjoint(s2))

# 세트.issubset(세트2) -> 세트2와의 부분집합 관계 여부 반환
result = set({1, 2, 3}).issubset(set({1, 2, 3, 4, 5}))
print(result)

# 세트.issuperset(세트2) -> 세트2와의 상위 집합 여부 반환
result = set({1, 2, 3, 4, 5}).issuperset(set({1, 2, 3}))
print(result)


# len(set) -> 세트의 요소 개수 반환
print(len(s_app))

# element in set
print("Netfilx" in s_app)
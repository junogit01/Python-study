# 딕셔너리 관련 함수
blackpink_info = {
    'member': ['제니', '로제', '지수', '리사'],
    'company' : 'YG',
    'age' : 20
}

# 딕셔너리.keys() -> 딕셔너리가 가진 모든 key를 반환 (dict_keys)
blackpink_keys = blackpink_info.keys()

# 딕셔너리.values() -> 딕셔너리가 가진 모든 value를 반환 (dict_values)
blackpink_values = blackpink_info.values()

# 딕셔너리.items() -> 딕셔너리가 가진 key, value를 각각 튜플로 묶어서 반환 (dict_items)
blackpink_items = blackpink_info.items()
for k,v in blackpink_items:
    print(f'key값 : {k}, value값 : {v}')

# 딕셔너리.clear() -> 딕셔너리 안의 모든 요소를 삭제한다.
blackpink_info.clear()
print(blackpink_info)

blackpink_info = {
    'member': ['제니', '로제', '지수', '리사'],
    'company' : 'YG',
    'age' : 20
}

# 딕셔너리.get(키) -> key에 대응되는 value를 반환 (key가 없으면, None)
# 딕셔너리.get(키, 기본값) -> key에 대응되는 value를 반환 (key가 없으면, default)
# print(blackpink_info["birth"]) --> 에러
print(blackpink_info.get("birth"))
print(blackpink_info.get("birth", "2023-10-27"))

# 키 in 딕셔너리 -> 딕셔너리 내 해당 key가 있는지 여부를 반환
print("age" in blackpink_info)
print("birth" in blackpink_info)
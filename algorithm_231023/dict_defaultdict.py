import collections

# 없는 키로 조회했을 경우, 에러를 출력하는 대신에 디폴트 값을 기준으로 생성해준다.
dict_a = collections.defaultdict(int)
dict_a['A'] = 5
dict_a['B'] = 4

print(dict_a)

# {'A': 5, 'B': 4, 'C': 0} 이 생성이 되고,
# {'A': 5, 'B': 4, 'C': 100} 으로 값이 증가
dict_a['C'] += 100 

print(dict(dict_a))
import collections

nums = "banana"
# 아이템에 대한 개수를 계산해서 딕셔너리(Counter)로 반환
dict_a = collections.Counter(nums)

# Counter의 기능 most_common(): 빈도수가 높은 요소를 반환
# 숫자 3을 인자로 하면, 상위 3개 요소를 반환
print(dict_a.most_common(2))
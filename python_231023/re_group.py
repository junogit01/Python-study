import re

match_obj = re.search('(\w+)\s+([0,1]{3}[-]\d{4}[-]\d{4})', '홍길동 010-1234-5678')
# (\w+) \s+ ([0,1]{3}[-]\d{4}[-]\d{4})

print(match_obj.group()) # 전체 출력
print(match_obj.group(0)) # 전체 출력
print(match_obj.group(1)) # 첫번째 그룹만 출력 (홍길동)
print(match_obj.group(2)) # 두번째 그룹만 출력 (010-1234-5678)
# print(match_obj.group(3)) 그룹 없음
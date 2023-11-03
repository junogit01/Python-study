import re

# 알파벳 소문자가 1개 이상 있는 문자열을 체크하는 정규식
# 정규식을 컴파일하고, 컴파일된 객체를 반환(c_re_obj)
c_re_obj = re.compile('[a-z]+')

# 컴파일된 객체를 이용해 search 함수를 사용
# search 함수 : 문자열 전체를 검색해 매치되는지 확인
# [매치 객체(match_obj) 반환 / 매치되지 않으면 None 반환] 
match_obj = c_re_obj.search('파이th0n')

# match_obj = re.search('[a-z]+','파이th0n')

print(match_obj)
print(match_obj.group()) # 매치된 문자열 반환
print(match_obj.start()) # 매치된 문자열의 시작 위치 반환
print(match_obj.end()) # 매치된 문자열의 끝 위치 반환
print(match_obj.span()) # 매치된 문자열의 (시작, 끝) 위치를 튜플로 반환

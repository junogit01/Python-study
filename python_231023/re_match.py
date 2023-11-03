import re

# 알파벳 소문자가 1개 이상 있는 문자열을 체크하는 정규식
# 정규식을 컴파일하고, 컴파일된 객체를 반환(c_re_obj)
c_re_obj = re.compile('[a-z]+')

# 컴파일된 객체를 이용해 match 함수를 사용
# match 함수 : 문자열의 처음부터 매치되는지 확인
# [매치 객체(match_obj) 반환 / 처음부터 매치되지 않으면 None 반환] 
match_obj = c_re_obj.match('pyth0n')

# match_obj = re.match('[a-z]+','pyth0n')

print(match_obj)
print(match_obj.group()) # 매치된 문자열 반환
print(match_obj.start()) # 매치된 문자열의 시작 위치 반환
print(match_obj.end()) # 매치된 문자열의 끝 위치 반환
print(match_obj.span()) # 매치된 문자열의 (시작, 끝) 위치를 튜플로 반환
import re

def is_palindrome(s: str) -> bool:
    # 문자, 숫자가 아닌 데이터만 찾아서, ''로 바꾸고, 소문자 전환
    target = re.sub('[^a-z0-9]', '', s.lower())
    return target == target[::-1]

str = "A man, a plan, a canal : Panama"
is_palindrome(str)
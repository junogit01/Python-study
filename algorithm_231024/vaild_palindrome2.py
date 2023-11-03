from collections import deque

def is_palindrome(s: str) -> bool:
    strs = deque([i for i in s.lower() if i.isalnum()])

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

str = "A man, a plan, a canal : Panama"
is_palindrome(str)




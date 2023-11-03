def is_palindrome(s: str) -> bool:
    strs = [i for i in s.lower() if i.isalnum()]
    # strs = []
    # for i in str.lower():
    #     if i.isalnum():
    #         strs.append(i)
    
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True

str = "A man, a plan, a canal : Panama"
is_palindrome(str)




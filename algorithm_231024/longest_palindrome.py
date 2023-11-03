def longest_palindrome(s:str) -> str:
    l_palindrome = ''
    for l in range(len(s)):
        for r in range(l, len(s)):
            sub_str = s[l:r+1]
            if sub_str == sub_str[::-1]:
                if len(sub_str) > len(l_palindrome):
                    l_palindrome = sub_str
    return l_palindrome

print(longest_palindrome("babad"))
def longest_palindrome(s:str) -> str:
    def check(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1  
        return s[left+1:right]
        
    l_palindrome = ''
    
    if len(s) < 2 or s == s[::-1]:
        l_palindrome = s
    else :
        for i in range(len(s)-1):
            # check(i, i+1) -> 짝수, 길이가 2인 펠린드롬을 찾고 확장해나간다.
            # check(i, i+2) -> 홀수, 길이가 3인 펠린드롬을 찾고 확장해나간다.
            
            # 길이를 기준으로 최대 길이를 구하는 방법!
            l_palindrome =  max(l_palindrome, check(i, i+1), check(i, i+2), key=len)
            
    return l_palindrome

print(longest_palindrome("babnolemonnomelonad"))
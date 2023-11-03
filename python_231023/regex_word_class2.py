import regex_check as rc

rc.match_check("a.b", "a0b") # 1번 T
rc.match_check("a.b", "a.b") # 2번 T 
rc.match_check("a.b", "aaab") # 3번 T
rc.match_check("a.b", "a\nb") # 4번 F
rc.match_check("a.b", "a\tb") # 5번 T
rc.match_check("a.b", "a   b") # 6번 F [.은 문자 하나!]
rc.match_check("a.b", "a b") # 7번 T
rc.match_check("a.b", "acb") # 8번 T
rc.match_check("a.b", "a\n\tb") # 9번 F

rc.match_check("a[.]b", "a.b") # 10번 T
rc.match_check("a[.]b", "a0b") # 11번 F
rc.match_check("a[.]b", "a\nb") # 12번 F

import regex_check as rc

rc.match_check("[abc]", "alphabet") # T
rc.match_check("[abc]", "liberty") # T
rc.match_check("[abc]", "digit") # F
rc.match_check("[0-9]", "123") # match_check("\d", "123") # T
rc.match_check("[^0-9]", "123") # match_check("\D", "123") # F
rc.match_check("[a-z]", "Alphabet") # T
rc.match_check("[a-zA-Z]", "Alphabet") # T
rc.match_check("[a-zA-Z0-9]", "GilDong123") # match_check("\w", "GilDong123") # T
rc.match_check("[^a-zA-Z0-9]", "GilDong123") # match_check("\W", "GilDong123") # F
rc.match_check("[\s]", "Hello World") # match_check("\s", "Hello World") # T
rc.match_check("[가-힣]", "홍길동") # T
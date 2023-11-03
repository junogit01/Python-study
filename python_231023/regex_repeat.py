import regex_check as rc

rc.match_check("go*d", "gd") # T
rc.match_check("go*d", "god") # T
rc.match_check("go*d", "goooooood") # T

rc.match_check("go+d", "gd") # F
rc.match_check("go+d", "god") # T
rc.match_check("go+d", "goooooood") # T

rc.match_check("g[A-Z]+d", "gOOOOOd") # T
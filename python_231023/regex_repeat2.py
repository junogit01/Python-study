import regex_check as rc

rc.match_check("hel{,3}o", "heo")
rc.match_check("hel{,3}o", "helo")
rc.match_check("hel{,3}o", "hello")
rc.match_check("hel{,3}o", "helllo")
rc.match_check("hel{,3}o", "hellllo") # F

rc.match_check("hel{3,}o", "hello") # F
rc.match_check("hel{3,}o", "helllo")
rc.match_check("hel{3,}o", "hellllo")

rc.match_check("go{0,}d", "gd") # match_check("go*d", "gd")
rc.match_check("go{1,}d", "gd") # match_check("go+d", "gd") # F
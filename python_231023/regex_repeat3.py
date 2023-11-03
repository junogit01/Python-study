import regex_check as rc

rc.match_check("hel{2}o", "hello")

rc.match_check("hel{1,3}o", "heo") # F
rc.match_check("hel{1,3}o", "helo")
rc.match_check("hel{1,3}o", "hello")
rc.match_check("hel{1,3}o", "helllo")
rc.match_check("hel{1,3}o", "hellllo") # F

rc.match_check("hell?o", "helo")
rc.match_check("hell?o", "hello")
rc.match_check("hell?o", "helllo") # F
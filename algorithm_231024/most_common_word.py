import re
from collections import Counter

def most_common_word(paragraph:str, banned:list[str]) -> str:
    # re.sub('정규식', '대체', '대상')
    p_list = re.sub("[\W]", ' ', paragraph.lower()).split()
    words = [word for word in p_list if word not in banned]        
    counter_words = Counter(words)
    return counter_words.most_common(1)[0][0]

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"] 

most_common_word(paragraph, banned)
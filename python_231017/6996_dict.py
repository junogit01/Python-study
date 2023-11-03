# 애너그램 - 딕셔너리 활용
test_count = int(input())
words = [input().split() for _ in range(test_count)]

for i in words:
    word1, word2 = i
    # word1 = word1.lower()
    # word2 = word2.lower()
    d_word1 = {}
    for j in word1:
        # 여기 부분1 (in)
        # key가 있으면, value에 +1, key가 없으면 생성(value = 1)
        if j in d_word1:
            d_word1[j] += 1
        else:
            d_word1[j] = 1
            
    d_word2 = {}
    for j in word2:
        # 여기 부분2 (in)
        # key가 있으면, value에 +1, key가 없으면 생성(value = 1)
        if j in d_word2:
            d_word2[j] += 1
        else:
            d_word2[j] = 1
    if d_word1 == d_word2 :
        print(f'{i[0]} & {i[1]} are anagrams')
    else :
        print(f'{i[0]} & {i[1]} are NOT anagrams')
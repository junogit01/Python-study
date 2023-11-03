# 애너그램 - 리스트 활용
test_count = int(input())
words = []
for _ in range(test_count):
    words.append(input().split())

for i in words:
    word1, word2 = i
    word1 = sorted(word1.lower())
    word2 = sorted(word2.lower())
    if word1 == word2 :
        print(f'{i[0]} & {i[1]} are anagrams')
    else :
        print(f'{i[0]} & {i[1]} are NOT anagrams')
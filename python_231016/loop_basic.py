for _ in range(5):
    print("홍길동 - for")

x = 0
while x < 5:
    print('홍길동 - while')
    x += 1
    
# range(처음, 끝, 단계)

# 테스트
print(list(range(10)))
print(list(range(1, 10+1)))
print(list(range(1, 10+1, 3)))

# # [위험!] 무한 루프
# while True:
#     print("반복반복")